import os

def loadinfo():
    # Load environment
    host = os.getenv('HOST')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')

    # Use defaults if no value specified
    if not host:
        host = "localhost"
    if not user:
        user = "root"
    if not password:
        password = "pass"

    # Return all values
    return host, user, password