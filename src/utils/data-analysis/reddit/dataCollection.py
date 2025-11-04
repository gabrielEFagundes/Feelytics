from redditClient import Client
from AI.jsonResumer import summarizeJson
from flask import jsonify
import json
import asyncio # on queue to implement, although it's extremely necessary

def getRedditData(topic):
    client = Client(
        "LYyabkq_WiRoEBvBNYMDyg",
        "0X8705Tt-GLhRUDn1di9J0QMrMpMlQ",
        "all"
    )

    userClient = client.defineClient()
    sub = client.defineSubreddit(userClient)

    data = []
    comments = []

    for i in sub.search(topic, limit=5):
        data.append({
            "title": i.title,
            "author": i.author.name if i.author else "Unknown",
            "context": i.selftext if i.selftext else 'None',
            "score": i.score,
        })

        if i.num_comments > 0:
            i.comments.replace_more(limit=10)
            for comm in i.comments.list()[:25]:
                cont = len(comments) + 1
                name = f"comment{cont}"
                comments.append({
                    name: {
                        "author": comm.author.name if comm.author else "Unknown",
                        "body": comm.body,
                    }
                })

            data.append(comments)

    return data

def turnDataIntoJson(data):
    jsObject = json.dumps(data)
    return summarizeJson(jsObject)