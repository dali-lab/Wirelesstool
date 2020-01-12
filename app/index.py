import json
import falcon


class Hello:
    def on_get(self, req, res):
        print("Hello!")


api = falcon.API()
api.add_route("/hello", Hello)
