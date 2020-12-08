from linked_list import *

from Linked_lists.linked_list import *


def defined_linked_list():
    testlist = singly_linked_list()
    testlist.head = node(1)
    testlist.listprint()
    testlist.append(2)
    testlist.listprint()
    testlist.append(3)
    testlist.append(5)
    testlist.insert(4, 4)
    testlist.listprint()
    testlist.head.printlist()
    return testlist


def defined_linked_list2():
    testlist = singly_linked_list()
    testlist.head = node(1)
    testlist.append(3)
    testlist.append(4)
    testlist.append(12)
    testlist.listprint()
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
    x = testlist.delete_node_pos(2)
    print(x)

    assert testlist.head.printlist() == [1, 2, 4, 5]


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
    
    im assuming positions 2 and 4
'''


def test_reverse_slice():
    testlist = defined_linked_list()
    testlist.reverse_slice(2, 4)
    assert testlist.head.printlist() == [1,4,3,2,5]


def test_swap_nodes():
    testlist = defined_linked_list()
    testlist.swap_nodes(2, 3)

    assert testlist.head.printlist() == [1, 3, 2, 4, 5]


def test_insertion_sort():
    testlist = defined_linked_list2()
    testlist.insertion_sort([5,2,7,6])
    assert testlist.head.printlist() == [1, 2, 3, 4, 5, 6, 7, 12]