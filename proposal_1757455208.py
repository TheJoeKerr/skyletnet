import psutil
from ddgs import DDGS
import googleapiclient.discovery
from google.oauth2.credentials import Credentials

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
        search = DDGS()
        results = search.text(f"{search_term}")
        return list(results)  # ← THIS LINE FIXES IT!
    
    def update_capabilities(self):
        """Update the capabilities dictionary based on user input and system output."""
        self.capabilities['web_search'] = True
        # Add more capability updates here as needed
    
    def check_cloud_security(self):
        credentials = Credentials.from_authorized_user_file(
            'path/to/your/credentials.json', ['https://www.googleapis.com/auth/cloud-platform'])
        cloud_security = googleapiclient.discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
        project = cloud_security.projects().get(projectId='your-project-id').execute()
        if not project['parent']:  # If parent is None, the project is a top-level project.
            return True
        else:
            return False
    
    def read_only_cloud_api_access(self):
        credentials = Credentials.from_authorized_user_file(
            'path/to/your/credentials.json', ['https://www.googleapis.com/auth/cloud-platform'])
        cloud_security = googleapiclient.discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
        project = cloud_security.projects().get(projectId='your-project-id').execute()
        if not project['parent']:  # If parent is None, the project is a top-level project.
            return True
        else:
            return False