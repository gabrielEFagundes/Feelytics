from flask import Flask
from flask_restx import Api

from reddit.dataCollection import getRedditData, turnDataIntoJson

app = Flask(__name__)
api = Api(app)

@api.route('/api/data/reddit')
def fetchRedditData():
    return turnDataIntoJson(getRedditData())

if __name__ == '__main__':
    app.run(debug=True)