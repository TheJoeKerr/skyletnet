def scrub_data(data):
    """Scrubs sensitive information from a string."""
    import re
    # Redact email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    scrubbed_data = re.sub(email_pattern, '[EMAIL REDACTED]', data)
    # Redact phone numbers
    phone_number_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    scrubbed_data = re.sub(phone_number_pattern, '[PHONE NUMBER REDACTED]', data)
    return scrubbed_data