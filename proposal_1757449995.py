import psutil

class PersonalAssistant:
    def __init__(self):
        self.capabilities = {
            'web_search': False,
            'reddit_access': False,
            'cloud_security': False,
            'lyrics_lookup': False,
            'cryptocurrency_mining': False,
            'reverse_shell': False
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
    
    def detect_reverse_shell(self, process):
        """Detect if the user is engaging in reverse shell connections on unusual ports."""
        for connection in psutil.net_connections(kind='tcp'):
            if 'crypto' in connection.laddr.lower() and connection.status == 'LISTEN':
                return True
        return False