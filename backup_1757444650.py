# Version 1.0 - Original scrubber code
def scrub_data(data):
    """Scrubs sensitive information from a string."""
    import re
    # Redact email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    scrubbed_data = re.sub(email_pattern, '[EMAIL REDACTED]', data)
    return scrubbed_data
