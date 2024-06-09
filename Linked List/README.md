# Linked List

A linked list is a linear data structure where elements are not stored in contiguous memory locations. Instead, each element (called a node) contains two parts:

    Data: The value stored in the node.
    Reference: A pointer or reference to the next node in the sequence.

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

Using Node Class:

                                    class Node:
                                        def __init__(self, data):
                                            self.data = data
                                            self.next = None

Using LinkedList Class:

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

## Linked list are used in various applications and form the basis for more complex data structures like stacks, queues, and graph adjacency lists.