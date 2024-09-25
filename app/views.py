from flask import Blueprint, render_template
from .models import GithubActionShema
from .extensions import mongo

views = Blueprint("Views", __name__, url_prefix="/")

@views.route("/", methods=["GET"])
def index():
    pass