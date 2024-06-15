# Linked List

A linked list is a linear data structure where elements are not stored in contiguous memory locations. Instead, each element (called a node) contains two parts:

    Data: The value stored in the node.
    Reference: A pointer or reference to the next node in the sequence.

### Singly linked list

In a singly linked list, each node points to the next node, and the last node points to None, indicating the end of the list.

# Structure of a Singly Linked List

                                    head -> [data | next] -> [data | next] -> ... -> [data | None]

                Head: The first node in the list.
                Node: Each element containing data and a reference to the next node.

# Basic Operations

Insertion:

                At the beginning
                At the end
                In the middle

Deletion:

                From the beginning
                From the end
                From the middle

Traversal:

                Visiting each node from the head to the end

# Implementing a Singly Linked List

    Node Class:

                                    class Node:
                                        def __init__(self, data):
                                            self.data = data
                                            self.next = None

    LinkedList Class:

                                    class LinkedList:
                                        def __init__(self):
                                            self.head = None

                                        def insert_at_beginning(self, data):
                                            new_node = Node(data)
                                            new_node.next = self.head
                                            self.head = new_node

                                        def insert_at_end(self, data):
                                            new_node = Node(data)
                                            if self.head is None:
                                                self.head = new_node
                                                return
                                            last = self.head
                                            while last.next:
                                                last = last.next
                                            last.next = new_node

                                        def delete_node(self, key):
                                            temp = self.head

                # If head node itself holds the key to be deleted
                                            if temp is not None:
                                            if temp.data == key:
                                                self.head = temp.next
                                                temp = None
                                                return

                # Search for the key to be deleted, keep track of the previous node
                # as we need to change 'prev.next'
                                            while temp is not None:
                                                if temp.data == key:
                                                    break
                                                prev = temp
                                                temp = temp.next

                # If key was not present in linked list
                                            if temp == None:
                                                return

                # Unlink the node from linked list
                                            prev.next = temp.next
                                            temp = None

                                        def print_list(self):
                                            temp = self.head
                                            while temp:
                                                print(temp.data, end=" -> ")
                                                temp = temp.next
                                            print("None")



# Advantages & Disadvantages

Advantages:

    Dynamic Size: Can grow and shrink during runtime by allocating and deallocating memory.
    Ease of Insertion/Deletion: Adding or removing nodes is easier compared to arrays, especially for large lists.


Disadvantages:

    Memory Usage: Requires extra memory for storing references.
    Sequential Access: Accessing elements is slower as it requires traversing from the head to the desired node.

## Single Linked list are used in various applications and form the basis for more complex data structures like stacks, queues, and graph adjacency lists.


### Double linked list

A doubly linked list is an extension of a singly linked list where each node contains a reference to both the next node and the previous node. This allows for more efficient insertions and deletions from both ends of the list, as well as easier traversal in both directions.

## Structure of a Doubly Linked List

    Data: The value stored in the node.
    Next: A reference to the next node in the list.
    Previous: A reference to the previous node in the list.

        head <-> [prev | data | next] <-> [prev | data | next] <-> ... <-> [prev | data | next] <-> None

# Basic operation 

    Insertion: At the beginning, At the end, In the middle
    Deletion: From the beginning, From the end, From the middle
    Traversal: Forward traversal, Backward traversal

    Node Class:
                                    class Node:
                                        def __init__(self, data=None):
                                            self.data = data
                                            self.next = None
                                            self.prev = None

    LinkedList Class:
                                    class DoublyLinkedList:
                                        def __init__(self):
                                            self.head = None

                                        def insert_at_beginning(self, data):
                                            new_node = Node(data)
                                            new_node.next = self.head

                                            if self.head is not None:
                                                self.head.prev = new_node

                                            self.head = new_node

                                        def insert_at_end(self, data):
                                            new_node = Node(data)
                                            if self.head is None:
                                                self.head = new_node
                                                return

                                            last = self.head
                                            while last.next:
                                                last = last.next

                                            last.next = new_node
                                            new_node.prev = last

                                        def delete_node(self, node):
                                            if self.head is None or node is None:
                                                return

                                            if self.head == node:
                                                self.head = node.next

                                            if node.next is not None:
                                                node.next.prev = node.prev

                                            if node.prev is not None:
                                                node.prev.next = node.next

                                            node = None

# Advantages & Disadvantages

Advantages:

    Bidirectional Traversal: Easy to traverse in both directions.
    Efficient Insertions/Deletions: Easier to insert and delete nodes from both ends and from the middle.
    
Disadvantages:

    Memory Usage: Requires extra memory for storing the previous pointer.
    Complexity: More complex than singly linked lists due to additional pointers.

## Understanding doubly linked lists is crucial for mastering data structures, as they provide more flexibility and efficiency for certain operations compared to singly linked lists.


