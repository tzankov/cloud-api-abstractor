from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from config import SitConfig
from aws import * 
from az import *
from resources import * 

application = Flask(__name__)
application.config.from_object(SitConfig())
api = Api(application)


class Actions(Resource):
    def __init__(self):
        self.available_actions = {
                            "create": ["ec2", "vm"],
                            "update": ["ec2", "vm"],
                            "secure": ["sg","nsg"],
                            }


    def get(self):
        return jsonify(self.available_actions)
        

    def post(self):
        posted_action = request.get_json()
        action = posted_action["action"]
        resource_type = posted_action["resource_type"]
        print(action)
        print(resource_type)
        if action in self.available_actions:
            ResourceFactory.build_resource(action, resource_type)
            return jsonify(str("Executing action: " + str(action) + " " + str(resource_type)))
        else:
            return jsonify({"error": "Action NOT FOUND"})


api.add_resource(Actions, "/api/v1/actions")


if __name__=="__main__":
    application.run()