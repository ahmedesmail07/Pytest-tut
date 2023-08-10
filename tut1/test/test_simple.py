from tut1.app.simple import add

#function should define with test_
def test_add():
    assert add(1,2) == 3


def test_sting_add():
    assert add("a","b") == "ab"

# class should also start with Test

class TestCase:
    def test_add(self):
        assert add(1,2) == 3


    def test_sting_add(self):
        assert add("a","b") == "ab"


