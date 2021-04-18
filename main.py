
# single Node of the linked list contains the data and points to the next node initially None
class Node:
    #default constructor
    def __init__(self,data):
        self.data = data
        self.next = None

# Linkedlist class

class Linkedlist():
    # default head points to the None
    #number of nodes to calculate the length of the linkedlist
    def __init__(self):
        self.head = None
        self.number_of_nodes = 0

    # method to return the length of the linkedlist
    def length_of_list(self):
        return self.number_of_nodes

    # method to insert element at the beginning of the list
    def insert_at_start (self , data):
        new_node = Node(data)
        self.number_of_nodes +=1

        #check if list is empty
        if not self.head:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    # method to insert  at the end of the linkedlist
    def insert_at_end(self,data):

        new_node = Node(data)
        self.number_of_nodes += 1
        actual_node = self.head

        while actual_node.next != None:
            actual_node = actual_node.next

        actual_node.next = new_node

    # method to traverse through the linkedlist

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next


    #method to insert node at any position in the list
    def insert_at_any(self, data , position):
        current = self.head
        new_node = Node(data)

        for i in range(position-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

L = Linkedlist()
L.insert_at_start(1)
L.insert_at_start(2)
L.insert_at_start(3)
L.insert_at_start(4)
L.insert_at_end(3)
print("length",L.number_of_nodes)
L.insert_at_any(5,2)
L.traverse()







