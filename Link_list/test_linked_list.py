from linked_list import *


def defined_linked_list():
    testlist = singly_linked_list
    testlist.head = node(1)
    testlist.listprint(testlist)
    testlist.append(testlist, 2)
    testlist.listprint(testlist)
    testlist.append(testlist, 3)
    testlist.append(testlist, 5)
    testlist.insert(testlist, 4, 4)
    testlist.listprint(testlist)
    testlist.head.printlist()
    return testlist
'''
    linked_list.delete_node(pos)

    example: 
    if pos is 3
    [1,2,3,4,5] => [1,2,4,5]

    if pos is not in list, return -1
'''
def test_delete_node():
    testlist = defined_linked_list()
    x = testlist.delete_node_pos(3)
    print(x)
    tempnode = testlist.head
    tempnode.printlist()
    assert tempnode.printlist() == [1,2,4,5]

'''
    linked_list.middle()

    example: 
    [1,2,3,4,5] => 3

    if list is empty return -1
'''
def test_middle():
    testlist = defined_linked_list()
    assert testlist.middle() == 3

def test_reverse():
    pass


'''
    tricky
    given n, m reverse linked list from m to n

    example: 
    if n = 2 and m = 4
    [1,2,3,4,5] => [1,4,3,2,5]
'''
def test_reverse_slice():
    pass

    

defined_linked_list()
test_delete_node(3)
