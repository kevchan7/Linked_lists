from datastructures import *


def test_stack():
    teststack = Stack([1, 2, 3, 4, 5])
    assert teststack.offload() == 1
    assert teststack.offload() == 2
    teststack.offload()
    teststack.offload()
    teststack.offload()
    assert teststack.list == []
    teststack.stacking(1)
    popstack3 = teststack.offload()
    assert popstack3 == 1
    assert teststack.list == []
def test_something():
    assert 1==1

test_stack()