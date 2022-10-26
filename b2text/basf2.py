"""Main module."""
from b2text.path import Path

def create_path():
    return Path()

def process(path):
    result = path.execute()
    print(result)
    pass