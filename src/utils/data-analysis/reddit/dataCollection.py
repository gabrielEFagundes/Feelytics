from redditClient import Client
import json

def getRedditData():
    client = Client(
        "LYyabkq_WiRoEBvBNYMDyg",
        "0X8705Tt-GLhRUDn1di9J0QMrMpMlQ",
        "AskReddit"
    )

    userClient = client.defineClient()
    sub = client.defineSubreddit(userClient)

    cont = 0
    data = []
    comments = []

    for i in sub.top(limit=1): # one's just for testing, our goal here is at least 50 to 100
        data.append({
            "title": i.title,
            "author": i.author.name if i.author else "Unknown",
            "context": i.selftext if i.selftext else 'None',
            "score": i.score,
        })

        if i.num_comments > 0:
            i.comments.replace_more(limit=5)
            for comm in i.comments.list():
                cont += 1
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
    print(jsObject)

turnDataIntoJson(getRedditData())