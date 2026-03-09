class Node:
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        
        curr , cidx = self.head , 0

        while curr and  cidx < index:
            cidx += 1
            curr = curr.next

        return curr.val if curr and index == cidx else -1

        
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        
    def addAtTail(self, val: int) -> None:
        
        if not self.head:
            self.head = Node(val)
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next

        temp = Node(val)
        curr.next = temp

    def addAtIndex(self, index: int, val: int) -> None:

        if not self.head and index == 0:
            self.head = Node(val)
            return

        dummy  = Node(None , self.head)
        prev , curr = dummy , self.head
        cidx = 0

        while curr and cidx < index:
            prev = prev.next
            curr = curr.next
            cidx += 1
        
        if cidx == index:
            temp = Node(val,curr)
            prev.next = temp

        self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        dummy  = Node(None , self.head)
        prev , curr = dummy , self.head
        cidx = 0

        while curr.next and cidx < index:
            prev = prev.next
            curr = curr.next
            cidx += 1
        
        if cidx == index:
            prev.next = curr.next

        self.head = dummy.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)