import psutil
from duckduckgo_search import DuckDuckGoSearch

class PersonalAssistant:
    def __init__(self):
        self.capabilities = {
            'web_search': False,
            'reddit_access': False,
            'cloud_security': False,
            'lyrics_lookup': False,
            'cryptocurrency_mining': False
        }
    
    def execute_task(self, task_description):
        """Safely execute a task for the user."""
        print(f"[SAFE EXECUTION] Task: {task_description}")
        return {"status": "requires_approval", "task": task_description}
    
    def detect_cryptocurrency_mining(self):
        """Detect if the user is mining cryptocurrencies."""
        for process in psutil.process_iter():
            if 'crypto' in process.name().lower():
                return True
        return False
    
    def web_search(self, search_term):
        """Search for information online using duckduckgo-search API."""
        search = DuckDuckGoSearch()
        results = search.query(f"{search_term}")
        for result in results:
            print(result)
    
    def update_capabilities(self):
        """Update the capabilities dictionary based on user input and system output."""
        self.capabilities['web_search'] = True