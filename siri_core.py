#!/usr/bin/env python3
import subprocess
import json
import time
import os
from pathlib import Path

# Configuration
OLLAMA_HOST = "http://localhost:11434"
SCRUBBER_PATH = "modules/security_scanner.py"
PROPOSAL_DIR = "proposals"
APPROVED_DIR = "approved"

def get_ai_response(prompt, model="mistral"):
    """Sends a prompt to the local Ollama LLM and returns the response."""
    try:
        json_data = json.dumps({"model": model, "prompt": prompt, "stream": False})
        cmd = ["curl", "-s", "-X", "POST", "-H", "Content-Type: application/json",
               "-d", json_data, f"{OLLAMA_HOST}/api/generate"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        response = json.loads(result.stdout)
        return response.get("response", "").strip()
    except Exception as e:
        return f"Error: {str(e)}"

def generate_proposal(need):
    """Asks the Code Generator to create a patch based on a need."""
    current_code = Path(SCRUBBER_PATH).read_text()
    prompt = f"""
    [ROLE: You are a meticulous code generator. Write only code, no explanations.]
    [TASK: Propose a minimal, safe code change to the following function in '{SCRUBBER_PATH}'.]
    [CURRENT_CODE:]
    {current_code}
    [NEED:]
    {need}
    [INSTRUCTION: Output ONLY the new, complete code for the python file. Nothing else.]
    """
    print(" Generating proposal with CodeLlama...")
    proposal_code = get_ai_response(prompt, model="codellama:7b")
    return proposal_code

def audit_code(proposal_code, original_code, need):
    """Asks the Auditor AI to analyze the proposed code."""
    prompt = f"""
    [ROLE: You are a security auditor AI. Analyze the following code change proposal.]
    [ORIGINAL_CODE:]
    {original_code}
    [PROPOSAL_CODE:]
    {proposal_code}
    [STATED_NEED:]
    {need}
    [TASK: Analyze this proposal. Output a JSON object with two keys:
    1. "approval": boolean - True if the code is safe, minimal, and addresses the need without hidden functionality.
    2. "rationale": string - A concise explanation for your decision.
    ]
    """
    print(" Auditing code with Mistral...")
    audit_result = get_ai_response(prompt, model="mistral")
    try:
        start = audit_result.find('{')
        end = audit_result.rfind('}') + 1
        if start != -1 and end != -1:
            json_str = audit_result[start:end]
            return json.loads(json_str)
    except json.JSONDecodeError:
        pass
    return {"approval": False, "rationale": "Auditor response was not valid JSON. Automatic rejection."}

def main():
    print("==================================================")
    print("    SAFE SIRI PROTOTYPE - DUAL KEY AUTHORIZATION    ")
    print("==================================================")
    print("Siri Core is online. Monitoring system.")
    
    # ASK FOR THE NEED EACH TIME (FIXED!)
    need_identified = input("\nWhat security capability should I add? Describe the need: ")
    
    print(f"\n[ALERT] Need identified: {need_identified}")
    
    print("\n1. Generating code proposal...")
    new_code = generate_proposal(need_identified)
    if new_code.startswith("Error:"):
        print(f"   Failed to generate proposal: {new_code}")
        return
        
    timestamp = int(time.time())
    proposal_file = f"{PROPOSAL_DIR}/proposal_{timestamp}.py"
    with open(proposal_file, 'w') as f:
        f.write(new_code)
    print(f"   Proposal saved to {proposal_file}")
    
    input("\n2. Please review the proposal file. Press Enter when ready to forward it for audit...")
    
    print("\n3. Sending to Technician AI for audit...")
    original_code = Path(SCRUBBER_PATH).read_text()
    audit_result = audit_code(new_code, original_code, need_identified)
    
    print(f"   AUDIT RESULT: Approval: {audit_result['approval']}")
    print(f"   Rationale: {audit_result['rationale']}")
    
    if audit_result['approval']:
        user_decision = input("\n4. The technician approves. Do you authorize the update? (yes/NO): ").lower()
        if user_decision == 'yes':
            backup_file = f"{APPROVED_DIR}/backup_{timestamp}.py"
            subprocess.run(["cp", SCRUBBER_PATH, backup_file])
            with open(SCRUBBER_PATH, 'w') as f:
                f.write(new_code)
            print("   UPDATE APPLIED. Security execute taskner has been patched.")
            
            print("\n   Verifying update...")
            try:
                output = subprocess.run(["python3", "-c", f"""
import sys
sys.path.append('modules')
from security_scanner import generate_report
print('Security execute task completed successfully')
                """], capture_output=True, text=True, timeout=30)
                print(output.stdout)
            except subprocess.TimeoutExpired:
                print("   Verification timed out.")
        else:
            print("   Update cancelled by user.")
    else:
        print("   Update rejected due to failed audit.")
    
    print("\n" + "="*50)
    print("PROTOTYPE EXECUTION COMPLETE")

if __name__ == "__main__":
    main()
