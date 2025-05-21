class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' -> ')
            temp = temp.next
        print("None")
        
    def append(self,value):
        add_node = Node(value)
        if self.head is None:
            self.head = add_node
        else:
            self.tail.next = add_node
        self.tail = add_node
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            ret = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return ret
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.length -=1
            temp.next = None
            if self.length == 0:
                self.tail = None
            return temp
    
    def get(self, index):
        temp = self.head
        if index >= self.length or index <0:
            return None
        else:
            for i in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        else: return False
    
    def insert(self, index, value):
        if index<0 or index>self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        elif index==self.length:
            return self.append(value)
        
        add_node = Node(value)
        prev = self.get(index -1)
        add_node.next = prev.next
        prev.next = add_node
        self.length+=1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index - 1)
        req = prev.next
        prev.next = req.next
        req.next = None
        self.length-=1
        return req

'''
my_list = Linkedlist(10)
my_list.append(20)
my_list.append(30)

my_list.print_ll()

print(my_list.pop())
my_list.print_ll()

my_list.prepend(9)
my_list.print_ll()
'''