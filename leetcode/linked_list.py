class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return self.val
    def __repr__(self):
        return self.val

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        i = 0
        if not self.head:
            self.head = ListNode(val)
            return val
        node = self.head


        while node.next:
            node = node.next
        node.next = ListNode(val)
        return val
    
    
    def out(self):
        if not self.head:
            return
        node = self.head
        while node.next:
            print(node.val)
            node = node.next
        print(node.val)

    def reverse(self):
        if not self.head:
            return
        current = self.head
        prev_node = None
        while current is not None:  # 1;
            next = current.next  # next=2; 
            current.next = prev_node # 2=
            prev_node = current
            current = next
        self.head = prev_node


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.out()

l.reverse()
l.out()