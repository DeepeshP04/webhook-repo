from flask import Blueprint, jsonify, render_template
from .models import GithubActionShema
from .extensions import mongo
from datetime import datetime

views = Blueprint("Views", __name__, url_prefix="/")

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/api/data")
def get_data():
    github_actions_data = list(mongo.db.github_actions.find())
    for action in github_actions_data:
        action["_id"] = str(action["_id"])
                   
    return jsonify(github_actions_data)

def format_datetime(datetime):
    formatted_datetime = datetime.strftime("%d %b %Y - %I:%M %p UTC")
    
    # Add the appropriate suffix for the day (st, nd, rd, th)
    day = datetime.day
    if 10 <= (day % 100) <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
      
    return formatted_datetime.replace(f"{day}", f"{day}{suffix}")    