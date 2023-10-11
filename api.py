from flask import Flask, request
from markupsafe import escape

"""basics"""
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/route")
def routing():
    return "<p>This is the routing page</p>"


"""
routing with dynamic routes
if the api route it's a string then flask routes automatically to the string route
if the api route is an int ONLY then it get's redirected to the API ID

"""


@app.route("/api/<api_route>")
def api_route(api_route):
    return f"this is the api route {escape(api_route)}"


@app.route("/api/<int:api_id>")
def api_route_int(api_id):
    return f"You are now at the API ID {api_id}"


"""
API GET/POST methods
To use the request methods you need to import the following:
"from flask import request"

to check whether the request is get or post you need to add into the app route the 
methods variable and decide if you want to accept only get or post or both
this is very important to define otherwise bad actors could abuse this and gain access
to our database!!!
"""


@app.route("/api/get", methods=["GET"])
def get_api_response():
    if request.method == "GET":
        return access_authorized()
    else:
        return access_denied()


@app.route("/api/post", methods=["POST"])
def post_api_response():
    if request.method == "POST":
        return access_authorized()
    else:
        return access_denied()


def access_denied():
    return "ACCESS DENIED"


def access_authorized():
    return "ACCESS AUTHORIZED"
