from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from flask_cors import CORS, cross_origin

from reddit.dataCollection import getRedditData, turnDataIntoJson

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r'/*': {"origins": "http://localhost:3000"}})

@cross_origin()
@api.route('/api/search', methods=['GET', 'POST'])
class SearchResource(Resource):
    def post(self):
        data = request.get_json()
        return data

@api.route('/api/data/reddit', methods=['GET'])
class RedditDataResource(Resource):
    def get(self):
        return turnDataIntoJson(getRedditData())

if __name__ == '__main__':
    app.run(port=5000)