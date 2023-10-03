class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        if data >= self.head.data:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next and data < current.next.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_list = LinkedList()
data = [6, 3, 4, 2, 1]

for num in data:
    my_list.insert_sorted(num)

my_list.display()
