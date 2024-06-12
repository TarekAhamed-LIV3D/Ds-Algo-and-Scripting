class Node:
    def __init__(self, data=None, next=None ):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __insert_at_begining__(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def __insert_at_end__(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
        
    def __insert_values__(self, data_list):
        self.head = None
        for data in data_list:
            self.__insert_at_end__(data)
            
    def __reset_the_list__(self):
        self.head = None
            
    def __delete_at__(self, index):
        if index < 0 or index>=self.__get_length__():
            raise Exception("This is  not a valid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
            
    def __insert_at__(self, index, data):
        if index < 0 or index>=self.__get_length__():
            raise Exception("This is  not a valid index")
        
        if index == 0:
            self.__insert_at_begining__(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break  
            itr = itr.next
            count += 1
        
    def __print__(self):
        if self.head is None:
            print("List is empty")
            return

        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        
        print(llstr)
        
    def __get_length__(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
        
if __name__ == '__main__':
    ll = LinkedList()
    print("-----After adding values from begining-----")
    ll.__insert_at_begining__(5)
    ll.__insert_at_begining__(50)
    ll.__insert_at_begining__(500)
    ll.__insert_at_begining__(5000)
    ll.__insert_at_begining__(50000)
    ll.__print__()
    ll.__reset_the_list__()
    print("-----After adding values from end-----")
    ll.__insert_at_end__(1)
    ll.__insert_at_end__(10)
    ll.__insert_at_end__(100)
    ll.__insert_at_end__(1000)
    ll.__insert_at_end__(10000)
    ll.__print__()
    print("-----After adding list of values-----")
    ll.__insert_values__(["Don't","Hit","The","Target","Right","Now",",","Over","&","Out"])
    ll.__print__()
    print("Length of the list = ", ll.__get_length__())
    ll.__delete_at__(0)
    print("-----List after deletation-----")
    ll.__print__()
    print("Length of the list = ", ll.__get_length__())
    print("-----List after adding-----")
    ll.__insert_at__(0,"Don't")
    ll.__print__()
    print("Length of the list = ", ll.__get_length__())