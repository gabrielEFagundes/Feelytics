from flask import Flask, jsonify
from flask_restx import Api, Resource

from reddit.dataCollection import getRedditData, turnDataIntoJson

app = Flask(__name__)
api = Api(app)

@api.route('/api/data/reddit', methods=['GET'])
class RedditDataResource(Resource):
    def get(self):
        return turnDataIntoJson(getRedditData())

if __name__ == '__main__':
    app.run(debug=True)