import json
import falcon
import psycopg2

# This classed is triggered by the "/test" endpoint
class Test:
    def on_get(self, req, res):
        print("This is a Falcon server with PostgreSQL!")

# Instantiate the server
api = falcon.API()

# Create a route called "/test" that will triger the Test class
api.add_route("/test", Test())