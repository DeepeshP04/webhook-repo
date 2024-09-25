from flask_pymongo import PyMongo

# Setup MongoDB here
DB_NAME = "database"
mongo = PyMongo()

def initialize_db(app):
    app.config["MONGO_URI"] = f"mongodb://localhost:27017/{DB_NAME}"
    mongo.init_app(app)