from logic import greet


def test_greet_name():
    assert greet("Rahim") == "Hello Rahim"

def test_greet_empty():
    assert greet("") == "Hello "

def test_add():
    assert add(2,3) == 5

def test_add_negative():
    assert add(-4,1) == -3