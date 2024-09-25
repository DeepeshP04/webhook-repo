// Initialize a variable to keep track of the last displayed timestamp.
let lastDisplayedTimestamp = null;

function fetchGithubActions() {
    // Fetch data from the API endpoint
    fetch('/api/data')
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
            let githubActionsHtml = ''; // Variable to hold the generated HTML for displaying actions
            let newActions = []; // Array to hold new actions that need to be displayed

            // Loop through each item in the fetched data
            data.forEach(item => {
                const actionTimestamp = new Date(item.timestamp); // Parse the item's timestamp

                // Check if the item is new (i.e., newer than the last displayed timestamp)
                if (lastDisplayedTimestamp === null || actionTimestamp > lastDisplayedTimestamp) {
                    newActions.push(item); // Add the new item to the array of new actions
                }
            });

            // Sort the new actions by timestamp in descending order (latest first)
            newActions.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

            // Generate HTML for each new action based on its type (push, pull request, merge)
            newActions.forEach(item => {
                if (item.action === "push") {
                    githubActionsHtml += `
                        <div class="card mb-2 bg-success">
                            <div class="card-body">
                                <h5 class="card-title">${item.author} pushed to ${item.to_branch} on ${formatDate(item.timestamp)}</h5>
                            </div>
                        </div>
                    `;
                } else if (item.action === "pull") {
                    githubActionsHtml += `
                        <div class="card mb-2 bg-info">
                            <div class="card-body">
                                <h5 class="card-title">${item.author} submitted a pull request from ${item.from_branch} to ${item.to_branch} on ${formatDate(item.timestamp)}</h5>
                            </div>
                        </div>
                    `;
                } else if (item.action === "merge") {
                    githubActionsHtml += `
                        <div class="card mb-2 bg-primary">
                            <div class="card-body">
                                <h5 class="card-title">${item.author} merged branch ${item.from_branch} to ${item.to_branch} on ${formatDate(item.timestamp)}</h5>
                            </div>
                        </div>
                    `;
                }
            });

            // Update the last displayed timestamp to the most recent one from the new actions
            if (newActions.length > 0) {
                lastDisplayedTimestamp = new Date(newActions[0].timestamp);
            }

            // Update the HTML content of the container to display the new actions
            document.getElementById("github-actions-container").innerHTML = githubActionsHtml;
        })
        .catch(error => console.error('Error fetching data:', error));
};

// Set an interval to fetch GitHub actions every 15 seconds
setInterval(fetchGithubActions, 15000);

// Call fetchGithubActions on window load to display the initial data
window.onload = fetchGithubActions;

// Function to format the date and time for display
function formatDate(dateTime) {
    const date = new Date(dateTime); // Create a Date object from the input timestamp
    const day = date.getDate(); // Get the day of the month
    const month = date.toLocaleString('en-US', { month: 'long' }); // Get the full month name
    const year = date.getFullYear(); // Get the year
    const time = date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }); // Format the time

    // Function to get the correct suffix for the day (st, nd, rd, th)
    let suffix;
    if (day >= 10 && day <= 20) {
        suffix = "th"; // Days 10-20 all get the "th" suffix
    } else {
        switch (day % 10) {
            case 1:
                suffix = "st"; // 1st
                break;
            case 2:
                suffix = "nd"; // 2nd
                break;
            case 3:
                suffix = "rd"; // 3rd
                break;
            default:
                suffix = "th"; // 4th and beyond get "th"
        }
    }

    // Return the formatted date string
    return `${day}${suffix} ${month} ${year} - ${time} UTC`;
}
