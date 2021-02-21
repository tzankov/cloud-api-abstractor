from flask import Flask, jsonify, request, make_response
from config import SitConfig
from aws import * 

app = Flask(__name__)
app.config.from_object(SitConfig())


@app.route('/api/v1/actions', methods=['GET'])
def api_all():
    available_actions = []
    for k,v in actions.items():
        available_actions.append(k)
    return jsonify(available_actions)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route("/api/v1/create", methods=["POST"])
def create_resource():
    if request.method=='POST':
        posted_action = request.get_json()
        action = posted_action['action']
        data = posted_action['data']
        if action in actions:
            eval(actions[action])
            return jsonify(str("Executing action: " + str(action)))
        else:
            return jsonify({'error': 'Action NOT FOUND'})


if __name__=='__main__':
    app.run(host=app.config['FLASK_RUN_HOST'], 
            port=app.config['FLASK_RUN_PORT'],
            )