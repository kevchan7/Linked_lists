from Linked_lists.datastructures import stack


class node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def printlist(self):
        nodeptr = self
        nodelist = [self.val,]
        while nodeptr.next:
            nodeptr = nodeptr.next
            nodelist = nodelist + [nodeptr.val]
        print(nodelist)
        return nodelist


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
        counter = pos - 1
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

    def reverse(self):
        nodeptr = self.head
        nodelist = stack([nodeptr])
        while nodeptr.next:
            nodelist.push(nodeptr.next)
            nodeptr = nodeptr.next
        newhead = nodelist.pop()
        nodeptr = nodelist.pop()
        newhead.next = nodeptr
        self.head.next = None
        while nodelist.list:
            nodeptr.next = nodelist.pop()
            nodeptr = nodeptr.next
        self.head = newhead

    def delete_node_pos(self,pos):
        nodeptr = self.head
        counter = pos - 1
        while counter > 0:
            nodeptr = nodeptr.next
            counter = counter - 1
        deleted_node_val = nodeptr.next.val
        tempnode = nodeptr.next.next
        nodeptr.next = tempnode
        return deleted_node_val

    def middle(self):
        counter = 0
        nodeptr = self.head
        while nodeptr.next:
            nodeptr = nodeptr.next
            counter = counter + 1
        print(counter)
        nodeptr = self.head
        counter2 = counter/2
        print(counter2)
        while counter2 > 0:
            nodeptr = nodeptr.next
            counter2 = counter2 - 1
        return nodeptr.val
    #def insertion_sort(self,input_array):
            #for next time
