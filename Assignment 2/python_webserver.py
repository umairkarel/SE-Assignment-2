"""
    This is a simple webserver implemented using Python Flask library

    Author: umairkarel
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """
        This is the home route for the server.
    """
    return "<h1>This is a simple Web-Server</h1>"


@app.route("/greet/<name>")
def greet(name):
    """
        This is a simple greet route which greets the user
        with the given name in the url parameter.
    """
    return f"<h1>Welcome to our simple server <i>{name}</i> </h1>"
    

if __name__ == "__main__":
    app.run(debug=True)