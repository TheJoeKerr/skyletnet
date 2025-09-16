import psutil
from ddgs import DDGS
import praw
from praw.reddit import Submission

class PersonalAssistant:
    def __init__(self):
        self.capabilities = {
            'web_search': True,
            'reddit_access': False,
            'cloud_security': False,
            'lyrics_lookup': False
        }
    
    def web_search(self, search_term):
        """Search for information online."""
        search = DDGS()
        results = search.text(f"{search_term}")
        return list(results)
    
    def reddit_access(self, subreddit, post_number=None):
        """Get a list of posts from a subreddit"""
        # Initialize the Reddit API wrapper
        reddit = praw.Reddit(client_id='your_client_id', client_secret='your_client_secret')
        
        # Search for the subreddit
        subreddit_obj = reddit.subreddit(subreddit)
        
        # Get the top posts from the subreddit
        if post_number is None:
            posts = subreddit_obj.hot(limit=None)
        else:
            posts = subreddit_obj.hot(limit=post_number)
        
        # Convert the Post objects to Submission objects
        submissions = [Submission(subreddit_obj, p.id) for p in posts]
        
        return submissions