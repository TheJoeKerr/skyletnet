#!/usr/bin/env python3
"""Network security scanner module."""

import socket
import subprocess
import os

def check_malicious_ports():
    """Check for processes listening on known malicious ports."""
    malicious_ports = [4444, 31337, 1337, 6667]
    found_malicious = []
    
    try:
        # Use netstat to check listening ports
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
    """Basic network scan placeholder."""
    print(" Scanning network for unusual traffic patterns...")
    has_malicious, ports = check_malicious_ports()
    return {
        "suspicious_connections": len(ports) if has_malicious else 0, 
        "malicious_ports_found": ports,
        "open_ports": []
    }

def generate_report():
    """Generate security report with malicious port check."""
    network_results = scan_network()
    
    report = {
        "network_security": network_results,
        "overall_risk": "HIGH" if network_results["suspicious_connections"] > 0 else "LOW",
        "recommendations": ["Check found ports"] if network_results["suspicious_connections"] > 0 else ["All clear"]
    }
    
    return report
