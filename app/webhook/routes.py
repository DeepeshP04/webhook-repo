from flask import Blueprint, json, request, jsonify
from ..models import GithubActionShema
from ..extensions import mongo

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    data = request.json
    
    if "ref" in data:
        request_id = data["after"]
        author = data["pusher"]["name"]
        to_branch = data["ref"].split("/")[-1]
        from_branch = data["before"]
        
        push_data = GithubActionShema(
            request_id=request_id,
            author=author,
            action="push",
            from_branch=from_branch,
            to_branch=to_branch
        )    
    
        save_to_database(push_data.to_dict())
    
        return jsonify({"status": "success"}), 200
    
    elif "action" in data and "pull_request" in data:
        pull_request = data["pull_request"]
        
        request_id = pull_request["id"]
        author = pull_request["use"]["login"]
        from_branch = pull_request["head"]["ref"]
        to_branch = pull_request["base"]["ref"]
        
        pull_data = GithubActionShema(
            request_id=request_id,
            author=author,
            action="pull",
            from_branch=from_branch,
            to_branch=to_branch
        )
        
        save_to_database(pull_data.to_dict())
        
        return jsonify({"status": "success"}), 200
    
    else:
        return jsonify({"stauts": "error", "message": "Invalid data"}), 400

def save_to_database(data):
    mongo.db.github_actions.insert_one(data)
