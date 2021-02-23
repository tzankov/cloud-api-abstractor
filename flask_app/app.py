from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from config import SitConfig
from aws import * 

application = Flask(__name__)
application.config.from_object(SitConfig())
api = Api(application)


class Actions(Resource):
    def __init__(self):
        self.available_actions = {
                            "create": "VPC",
                            "create": "VNET",
                            "peer": "VNET/VPC"
                            }


    def get(self):
        return jsonify(self.available_actions)
        

    def post(self):
        posted_action = request.get_json()
        action = posted_action['action']
        resource_type = posted_action['resource_type']
        if action in self.available_actions:
            ResourceFactory.build_resource(action, resource_type)
            return jsonify(str("Executing action: " + str(action) + str(resource_type)))
        else:
            return jsonify({'error': 'Action NOT FOUND'})


api.add_resource(Actions, '/api/v1/actions')


if __name__=='__main__':
    application.run()