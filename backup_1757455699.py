import psutil
from ddgs import DDGS

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
