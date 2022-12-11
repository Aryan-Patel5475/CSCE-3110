class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse_list(self):

        prev_node = None
        node = self.head

        while node is not None:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        self.head = prev_node

    def print_list(self):

        node = self.head

        while node is not None:
            print(node.data)
            node = node.next

linklist = LinkedList()

linklist.prepend('D')
linklist.prepend('C')
linklist.prepend('B')
linklist.prepend('A')

linklist.print_list()
print()

linklist.reverse_list()
linklist.print_list()