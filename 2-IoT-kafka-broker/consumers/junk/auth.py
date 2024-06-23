import base64

username = "ditto"
password = "ditto"
credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()
print(f"Basic {encoded_credentials}")

