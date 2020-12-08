from Linked_lists.datastructures import stack


class node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def printlist(self):
        nodeptr = self
        nodelist = [self.val, ]
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

    def insert(self, newval, pos):  # pos.next is where the new node will be
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

    def delete_node_pos(self, pos):
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
        counter2 = counter / 2
        print(counter2)
        while counter2 > 0:
            nodeptr = nodeptr.next
            counter2 = counter2 - 1
        return nodeptr.val

    def insertion_sort(self,input_array):
        for x in input_array:
            new_node = node(x)
            cursor = self.head
            if x < cursor.val:
                new_node.next = cursor
                self.head = new_node
            else:
                while x > cursor.val | cursor.next:
                    prev = cursor
                    cursor = cursor.next
                prev.next = new_node
                new_node.next = cursor


    # for next time

    def swap_nodes(self, a, b):
        cursor = self.head
        a_exist = False
        b_exist = False
        while cursor.next:
            cursor = cursor.next
            if cursor.val == a:
                a_exist = True
                print("a exists")
            if cursor.val == b:
                b_exist = True
                print("b exists")
        if a_exist & b_exist:
            cursor = self.head
            while cursor.next:
                if cursor.val == a:
                    cursor.val = b
                elif cursor.val == b:
                    cursor.val = a
                cursor = cursor.next
        else:
            print(a," and ", b, " do not exist within linked list")

    def reverse_slice(self, n, m):
        cursor = self.head
        counter = n - 2
        while counter > 0:
            cursor = cursor.next
            counter -= 1
        cutoff = cursor
        counter = m - n + 1
        while counter > 0:
            cursor = cursor.next
            counter -= 1
        prev = cursor.next  # finding the tail of the linked list
        cursor = cutoff.next
        counter = m - n

        while counter > 0:
            next_node = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = next_node
            counter -= 1
        cutoff.next = cursor
        cursor.next = prev


