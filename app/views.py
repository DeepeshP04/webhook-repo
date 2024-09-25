from flask import Blueprint, jsonify, render_template
from .extensions import mongo

views = Blueprint("views", __name__, url_prefix="/")

# Route for the home page
@views.route("/")
def index():
    return render_template("index.html")

# Route to fetch GitHub actions data from the MongoDB database
@views.route("/api/data")
def get_github_actions_data():
    github_actions_data = list(mongo.db.github_actions.find())
    
    # Convert MongoDB ObjectId to string for JSON serialization
    for action in github_actions_data:
        action["_id"] = str(action["_id"])
                   
    return jsonify(github_actions_data) 