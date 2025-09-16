import psutil
from ddgs import DDGS

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

    def monitor_critical_files(self):
        """Monitor critical system files for changes."""
        while True:
            for file in CRITICAL_FILES:
                if not os.path.isfile(file) or md5sum(file) != CHECKSUM[file]:
                    # File is missing/changed, take appropriate action
                    self.capabilities['cloud_security'] = True
                    break
            else:
                # No critical files are missing or changed
                self.capabilities['cloud_security'] = False
            time.sleep(60)  # Check every minute

CRITICAL_FILES = [
    '/bin/bash',
    '/usr/sbin/sshd',
    '/etc/passwd',
    '/etc/shadow'
]
CHECKSUM = {file: hashlib.md5(open(file, 'rb').read()).hexdigest() for file in CRITICAL_FILES}