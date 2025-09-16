import psutil
from monitor import Monitor

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
    
    def monitor_passwd(self):
        """Monitor changes to /etc/passwd"""
        with open("/etc/passwd", "r") as f:
            lines = f.readlines()
        
        while True:
            with open("/etc/passwd", "r") as f:
                new_lines = f.readlines()
            
            if len(new_lines) != len(lines):
                return True
            
    def run(self):
        """Run the Personal Assistant."""
        while True:
            task_description = input("Enter task description: ")
            result = self.execute_task(task_description)
            print(f"Result: {result}")

monitor = Monitor("/etc/passwd")
personal_assistant = PersonalAssistant()
while True:
    personal_assistant.run()