class node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class singly_linked_list:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval:
            print(printval.val)
            printval = printval.next

    def new_head(self, newheadval):
        newhead = node(newheadval)
        newhead.next = self.head
        self.head = newhead

    def append(self, newval):
        newnode = node(newval)
        nodeptr = self.head
        while nodeptr.next:
            nodeptr = nodeptr.next
        nodeptr.next = newnode

    def insert(self, newval, pos): # pos.next is where the new node will be
        insertnode = node(newval)
        counter = pos
        nodeptr = self.head
        while counter > 1:
            nodeptr = nodeptr.next
            counter = counter - 1
        insertnode.next = nodeptr.next
        nodeptr.next = insertnode

    def position(self, pos):
        nodeptr = self.head
        while pos > 1:
            nodeptr = nodeptr.next
            pos = pos - 1
        return nodeptr.val
