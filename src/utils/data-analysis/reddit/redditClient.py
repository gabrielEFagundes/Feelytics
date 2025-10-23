import praw

class Client:
    def __init__(self, id, secret, subreddit):
        self.id = id
        self.secret = secret
        self.agent = "Feelytics' Data Analysis for Reddit"
        self.subreddit = subreddit

    def defineClient(self):
        client = praw.Reddit(
            client_id=self.id,
            client_secret=self.secret,
            user_agent=self.agent,
        )

        return client
    
    def defineSubreddit(self, client):
        return client.subreddit(self.subreddit)