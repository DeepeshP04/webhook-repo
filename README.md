# Webhook Receiver

## Overview

This repository is for handling various GitHub events, saves the data in mongodb database and displays through a Flask application with a front-end built using HTML and JavaScript.

## Features

- **Receive Webhook Events**: The application can receive various GitHub events (e.g., push, pull request, merge events).
- **Store Event Data**: Captures and stores webhook event data in a MongoDB database using PyMongo.
- **User Interface**: Provides a simple web interface built with HTML and JavaScript for testing webhook functionality and viewing received events.
- **Real-time Updates**: Utilizes JavaScript to update the user interface in real-time as events are received.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **MongoDB**: A NoSQL database for storing webhook event data.
- **PyMongo**: A Python library for interacting with MongoDB.
- **HTML**: For structuring the web interface.
- **JavaScript**: For client-side scripting and real-time updates.

## Getting Started

### Prerequisites

- Python 3.x
- MongoDB
- GitHub account

### Installation

1. **Clone the repository**:

   git clone repo-url
   cd webhook-repo

2. **Create a virtual environment**:

    python -m venv venv
    source venv\Scripts\activate  # On macOS use venv/bin/activate

3. **Install requirements**:

    pip install -r requirements.txt

4. **Run the flask application**:

    python run.py
    



