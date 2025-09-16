#!/usr/bin/env python3
     """Network security scanner module."""
     
     import os
     import time
     import subprocess
     import hashlib
     
     def check_malicious_ports():
         """Check for processes listening on known malicious ports."""
         malicious_ports = [4444, 31337, 1337, 6667]
         found_malicious = []
         
         try:
             result = subprocess.run(['netstat', '-tuln'], capture_output=True, text=True)
             lines = result.stdout.split('\n')
             
             for line in lines:
                 for port in malicious_ports:
                     if f':{port} ' in line:
                         found_malicious.append(port)
                         
             return bool(found_malicious), found_malicious
             
         except Exception as e:
             return False, [f"Error: {str(e)}"]
     
     def scan_network():
         """Basic network scan."""
         has_malicious, ports = check_malicious_ports()
         return {
             "suspicious_connections": len(ports),
             "malicious_ports_found": ports,
             "open_ports": []
         }
     
     def monitor_passwd():
         """Monitor /etc/passwd file for changes."""
         try:
             current_time = int(time.time())
             mtime = os.path.getmtime('/etc/passwd')
             
             if current_time - mtime < 5:
                 return "ALERT: /etc/passwd has been recently modified"
             
             return "/etc/passwd appears unchanged"
             
         except Exception as e:
             return f"Error: {str(e)}"
     
     def monitor_critical_files():
        """Monitor critical files for existence"""
         try:
            if not os.path.exists('/bin/bash'):
                raise FileNotFoundError('File /bin/bash is missing')
            
            if not os.path.exists('/usr/bin/sudo'):
                raise FileNotFoundError('File /usr/bin/sudo is missing')
            
            if not os.path.exists('/etc/passwd'):
                raise FileNotFoundError('File /etc/passwd is missing')
             
            # Add SHA256 checksum verification
            passwd_checksum = hashlib.sha256(open('/etc/passwd', 'rb').read()).hexdigest()
            if not os.path.exists('passwd.sha256') or open('passwd.sha256').read().strip() != passwd_checksum:
                raise FileNotFoundError('File /etc/passwd has been modified')
             
            return '/bin/bash, /usr/bin/sudo, and /etc/passwd are present'
         except Exception as e:
             return f"Error: {str(e)}"
     
     def generate_report():
         """Generate security report."""
         network_results = scan_network()
         passwd_status = monitor_passwd()
         critical_files_status = monitor_critical_files()
         
         report = {
             "network_security": network_results,
             "passwd_monitor": passwd_status,
             "critical_files_monitor": critical_files_status,
             "overall_risk": "HIGH" if network_results["suspicious_connections"] > 0 or passwd_status != '/etc/passwd appears unchanged' else "LOW",
             "recommendations": ["Check found ports", "Check for missing critical files"] if network_results["suspicious_connections"] > 0 or passwd_status != '/etc/passwd appears unchanged' else ["All clear"]
         }
         
         return report
     
     # Test the functions
     if __name__ == "__main__":
         print("Testing security scanner...")
         report = generate_report()
         import json
         print(json.dumps(report, indent=2))