from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from flask_cors import CORS, cross_origin

from dataCollection import getRedditData, turnDataIntoJson

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r'/*': {"origins": "http://localhost:3000"}})

def requestSearch(search):
    data = []
    data.append(search)
    print(data[0]['request'])
    return data

@cross_origin()
@api.route('/api/search', methods=['GET', 'POST'])
class SearchResource(Resource):
    def get(self):
        return
    
    def post(self):
        search = request.get_json()
        requestSearch(search)

@api.route('/api/data/reddit', methods=['GET'])
class RedditDataResource(Resource):
    def get(self):
        return turnDataIntoJson(getRedditData("renan"))

if __name__ == '__main__':
    app.run(port=5000)