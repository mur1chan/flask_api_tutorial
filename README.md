# flask_api_tutorial
This is a simple Flask API project that demonstrates how to use basics like routing, dynamic routes and HTTP methods (GET, POST) in Flask.
Installation

Install the required packages:

    pip install -r requirements.txt

Use

Start the server with the following command:


    python app.py

The server should now be running and accessible at http://127.0.0.1:5000/.
Endpoints

    GET /: Returns "Hello, World!".
    GET /route: Returns routing information.
    GET /api/<api_route>: Returns information about a dynamic API route.
    GET /api/<int:api_id>: Returns information about an API ID.
    GET /api/get: An endpoint that accepts only GET requests.
    POST /api/post: An endpoint that accepts only POST requests.


to test the methods you can use the request_api.py to learn more about it.
