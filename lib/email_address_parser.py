import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Remove leading/trailing whitespace, collapse multiple spaces
        cleaned = re.sub(r'\s+', ' ', self.addresses.strip())

        # Split by comma OR space (handle both delimiters)
        parts = re.split(r'[,\s]+', cleaned)

        # Match only valid emails
        valid_emails = [email for email in parts if re.fullmatch(r"[\w\.-]+@[\w\.-]+\.\w+", email)]

        # Remove duplicates and return sorted list
        return sorted(set(valid_emails))
