function fetchGithubActions() {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            let githubActionsHtml = '';
            data.forEach(item => {

                if (item["action"] === "push") {
                    githubActionsHtml += `
                        <div class="card mb-2 bg-success">
                            <div class="card-body">
                                <h5 class="card-title">${item["author"]} pushed to ${item["to_branch"]} on ${formatDateTime(item["timestamp"])}</h5>
                            </div>
                        </div>
                    `
                } else if (item["action"] === "pull") {
                    githubActionsHtml += `
                        <div class="card mb-2 bg-info">
                            <div class="card-body">
                                <h5 class="card-title">${item["author"]} submitted a pull request from ${formatDateTime(item["from_branch"])} to ${item["to_branch"]} on ${item.timestamp}</h5>
                            </div>
                        </div>
                    `
                } else if (item["action"] === "merge") {
                    githubActionsHtml += `
                        <div class="card mb-2 bg-primary">
                            <div class="card-body">
                                <h5 class="card-title">${item["author"]} merged branch ${item["from_branch"]} to ${item["to_branch"]} on ${formatDateTime(item["timestamp"])}</h5>
                            </div>
                        </div>
                    `
                }
        })
        document.getElementById("github-actions-container").innerHTML = githubActionsHtml
    })
    .catch(error => console.error('Error fetching data:', error));
};

setInterval(fetchGithubActions, 15000);

window.onload = fetchGithubActions;

function formatDateTime(dateTime) {
    if (!(dateTime instanceof Date)) {
        if (typeof dateTime === 'string') {
          dateTime = new Date(dateTime);
        } else if (typeof dateTime === 'number') {
          dateTime = new Date(dateTime * 1000);
        } else {
          throw new Error('Invalid dateTime value');
        }
    }
    
    const day = dateTime.getDate();
    let suffix;
    
    if (day >= 10 && day <= 20) {
      suffix = "th";
    } else {
      switch (day % 10) {
        case 1:
          suffix = "st";
          break;
        case 2:
          suffix = "nd";
          break;
        case 3:
          suffix = "rd";
          break;
        default:
          suffix = "th";
      }
    }
    
    const formattedDateTime = dateTime.toLocaleString("en-US", {
      year: "numeric",
      month: "short",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    }).replace(`${day}`, `${day}${suffix}`);
    
    return formattedDateTime + " UTC";
  }