from flask import Flask, jsonify, request
from flask_restx import Api, Resource, reqparse
from flask_cors import CORS, cross_origin

from dataCollection import getRedditData, turnDataIntoJson

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r'/*': {"origins": "http://localhost:3000"}}) # remember to change this when in production!

parser = reqparse.RequestParser()
parser.add_argument('query', help='No query parsed!', required=True)

searchQuery = []

@cross_origin()
@api.route('/api/data/reddit', methods=['GET', 'POST'])
class RedditDataResource(Resource):
    def get(self):
        return jsonify({ 'error': 'Sorry, you cannot make requisitions directly through the URL, try out our API or use the platform!' })

    def post(self):
        args = parser.parse_args()
        return turnDataIntoJson(getRedditData(request.args.get('query')))

if __name__ == '__main__':
    app.run(port=5000)