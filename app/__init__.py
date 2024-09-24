from flask import Flask

from app.webhook.routes import webhook
from app.extensions import mongo

# Creating our flask app
def create_app():

    app = Flask(__name__)
    
    # registering all the blueprints
    app.register_blueprint(webhook)
    
    mongo.init_app(app)
    
    return app