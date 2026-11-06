from logic import greet

def test_greet():
    assert greet() == "Hello world"


def test_greet_name():
    assert greet("Rahim") == "Hello Rahim"

def test_greet_empty():
    assert greet("") == "Hello "