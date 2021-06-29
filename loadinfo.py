import os

def loadinfo():
    # Load environment
    host = os.getenv('HOST')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    source = os.getenv('SOURCE')
    destination = os.getenv('DESTINATION')

    # Use defaults if no value specified
    if not host:
        host = "localhost"
    if not user:
        user = "root"
    if not password:
        password = "pass"
    if not source:
        source = "reddit.csv"
    if not destination:
        destination = "reddit"

    # Return all values
    return host, user, password, source, destination