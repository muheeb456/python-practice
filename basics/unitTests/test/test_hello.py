from hello import hello

def test_argument():
    assert hello("muheeb") == "hello, muheeb"

def test_default():
    assert hello() == "hello, world"