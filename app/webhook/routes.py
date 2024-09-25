from flask import Blueprint, json, request, jsonify
from ..models import GithubActionSchema
from ..extensions import mongo

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

# Route to receive GitHub webhook events
@webhook.route('/receiver', methods=["POST"])
def receiver():
    data = request.json
    
    # Check for push events
    if "ref" in data:
        request_id = data["after"]
        author = data["pusher"]["name"]
        to_branch = data["ref"].split("/")[-1] 
        from_branch = data["before"]
        
        push_data = GithubActionSchema(
            request_id=request_id,
            author=author,
            action="push",
            from_branch=from_branch,
            to_branch=to_branch
        )    
    
        save_to_database(push_data.to_dict())
    
        return jsonify({"status": "success"}), 200
    
    # Check for pull request events
    elif "action" in data and "pull_request" in data:
        action_type = data["action"]
        pull_request = data["pull_request"]
        
        request_id = pull_request["id"]
        author = pull_request["user"]["login"]
        from_branch = pull_request["head"]["ref"]
        to_branch = pull_request["base"]["ref"]
        
        pull_data = GithubActionSchema(
            request_id=request_id,
            author=author,
            action="pull",
            from_branch=from_branch,
            to_branch=to_branch
        )
        
        save_to_database(pull_data.to_dict())
        
         # If the pull request was closed and merged, save a merge event
        if action_type == "closed" and pull_request.get("merged"):
        
            merge_data = GithubActionSchema(
                request_id=request_id,
                author=author,
                to_branch=to_branch,
                from_branch=from_branch,
                action="merge"
            )
            save_to_database(merge_data.to_dict())
        
        return jsonify({"status": "success"}), 200
        
    else:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

def save_to_database(data):
    mongo.db.github_actions.insert_one(data)
