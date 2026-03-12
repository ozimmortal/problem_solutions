class Node:
    
    def __init__(self,val,next=None):
        self.val = val
        self.next =next


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.c = 0
        self.k = k
        

    def insertFront(self, value: int) -> bool:
        if self.c < self.k:
            dummy = Node(0,self.head)
            t = Node(value ,dummy.next)
            self.head = t
            self.c += 1
            return True

        return False

    def insertLast(self, value: int) -> bool:
        if self.c < self.k:
            dummy = Node(0,self.head)
            t = Node(value)
            curr = dummy
            while curr.next:
                curr = curr.next
            curr.next = t
            self.head = dummy.next
            self.c += 1

            return True
        return False

    def deleteFront(self) -> bool:
        if self.c:
            dummy = Node(0,self.head)
            dummy.next = self.head.next
            self.head = dummy.next

            self.c -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.c:
            dummy = Node(0,self.head)
            curr = dummy
            while curr.next and curr.next.next:
                curr = curr.next
            curr.next = None
            self.head = dummy.next
            self.c -= 1
            return True
        return False
    def getFront(self) -> int:
        if self.c != 0:
            return self.head.val
        return -1
    def getRear(self) -> int:
        if self.c != 0:
            curr = self.head
            while curr.next:
                curr = curr.next
            return curr.val
        return -1
        
    def isEmpty(self) -> bool:
        return self.c == 0

    def isFull(self) -> bool:
        return self.c == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()