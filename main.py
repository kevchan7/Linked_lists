from linked_list import *


def test_linkedlist():
    testlist = singly_linked_list
    testlist.head = node(1)
    testlist.listprint(testlist)
    testlist.append(testlist,2)
    testlist.listprint(testlist)
    testlist.append(testlist,3)
    testlist.append(testlist,5)
    testlist.insert(testlist,4,3)
    testlist.listprint(testlist)
    assert testlist.position(testlist,4) == 4
    testlist.new_head(testlist,0)
    testlist.listprint(testlist)
    tempnode = testlist.head
    assert tempnode.printlist() == [0,1,2,3,4,5]
    testlist.reverse(testlist)
    assert testlist.head.printlist() == [5,4,3,2,1,0]
    testlist.listprint(testlist)


test_linkedlist()
