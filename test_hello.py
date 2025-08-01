from hello import hello

def test_hello():
    assert hello("Raj") == "hello, Raj"
    assert hello() == "hello, world"

# so to do this hello function from hello.py should return and not print
