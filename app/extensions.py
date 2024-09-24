from flask_pymongo import PyMongo

# Setup MongoDB here
DB_NAME = "database"

mongo = PyMongo(uri=f"mongodb://localhost:27017/{DB_NAME}")