import praw

client = praw.Reddit(
    client_id="LYyabkq_WiRoEBvBNYMDyg",
    client_secret="0X8705Tt-GLhRUDn1di9J0QMrMpMlQ",
    user_agent="Feelytics' Data Analysis for Reddit",
)

sub = client.subreddit("AskReddit")

data = []

for i in sub.top(limit=10):
    data.append({
        "title": i.title,
        "author": i.author.name if i.author else "Unknown",
        "score": i.score,
    })

    if i.num_comments > 0:
        i.comments.replace_more(limit=5)
        for comm in i.comments.list():
            data.append({
                "comments": {
                    "author": comm.author.name if comm.author else "Unknown",
                    "body": comm.body,
                }
            })