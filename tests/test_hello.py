from src.hello import greet

def test_greet():
    assert greet("World") == "Hello, World!"

def test_greet_engineer():
    assert greet("Engineer") == "Hello, Engineer!"