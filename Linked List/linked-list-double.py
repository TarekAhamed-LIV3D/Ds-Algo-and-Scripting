class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def __append__(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            curl = self.head
            while curl.next:
                curl = curl.next
            curl.next = new_node
            new_node.prev = curl
            new_node.next = None
            
    def __prepend__(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
            
    def add_after_node(self, key, data):
        curl = self.head
        while curl:
            if curl.data == key:
                new_node = Node(data)
                nxt = curl.next
                curl.next = new_node
                new_node.prev = curl
                if nxt:
                    new_node.next = nxt
                    nxt.prev = new_node
                return
            curl = curl.next
        
    
    def add_before_node(self, key, data):
        curl = self.head
        while curl:
            if curl.prev is None and curl.data == key:
                self.__prepend__(data)
                return
            elif curl.data == key:
                new_node = Node(data)
                prev = curl.prev
                prev.next = new_node
                curl.prev = new_node
                new_node.next = curl 
                new_node.prev = prev
            curl = curl.next
    
    def __print__(self):
        curl = self.head
        while curl:
            print(curl.data)
            curl = curl.next
    
    def printlist(self):
        if self.head is None:
            print("List is empty")
            return

        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        
        print(llstr)
    
dll = DoubleLinkedList()
dll.__append__(10)
dll.__append__(100)
dll.__append__(1000)
dll.__append__(10000)
dll.__append__(100000)
print("Linked list after appending...")
dll.printlist()
dll.__prepend__(20)
dll.__prepend__(200)
dll.__prepend__(2000)
dll.__prepend__(20000)
dll.__prepend__(200000)
print("Linked list after prepending...")
dll.printlist()
dll.add_after_node(10, 11)
dll.add_after_node(20, 22)
dll.add_after_node(1000, 333)
print("Linked list after adding nodes...")
dll.printlist()
dll.add_before_node(10, 11)
dll.add_before_node(20, 22)
dll.add_before_node(1000, 333)
print("Linked list before adding nodes...")
dll.printlist()