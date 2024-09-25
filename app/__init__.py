from flask import Flask

from app.webhook.routes import webhook
from .views import views
from app.extensions import initialize_db

# Creating our flask app
def create_app():

    app = Flask(__name__)
    
    # registering all the blueprints
    app.register_blueprint(webhook)
    app.register_blueprint(views)
    
    initialize_db(app)
    
    return app