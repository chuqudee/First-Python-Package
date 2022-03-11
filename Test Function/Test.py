from MyPackage import Mymodule 

def test_top_n():
    """
    make sure top_n works correctly
    """
    
    assert Mymodule.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert Mymodule.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert Mymodule.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'


def test_fibonacci():
    """
    make sure fibonacci works correctly
    """

    assert Mymodule.fibonacci(8) == 21, 'incorrect'
    assert Mymodule.fibonacci(3) == 2, 'incorrect'
    assert Mymodule.fibonacci(5) == 5, 'incorrect'
    