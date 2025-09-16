import psutil
from ddgs import DDGS
from google.cloud import securitycenter

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
        
    def cloud_security(self, project_id: str):
        """Checks the security status of a Google Cloud project using the Cloud Security Command Center API"""
        scanner = securitycenter.SecurityCenterClient()
        project_name = f"projects/{project_id}"
        response = scanner.list_findings(parent=project_name)
        for finding in response:
            print(finding)