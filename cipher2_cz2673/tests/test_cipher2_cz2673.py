from cipher2_cz2673 import __version__
from cipher2_cz2673 import cipher2_cz2673

def test_version():
    assert __version__ == '0.1.0'

def test_negative_shift():
    #args = ("hello", 1)
    expected = 'XY'
    *args , = ['hi', -10]
    #shift = 1
    actual = cipher2_cz2673.cipher(*args)
    print(actual)
    assert actual == expected, "should be fg" #If the test failed, assertion error will be raised
