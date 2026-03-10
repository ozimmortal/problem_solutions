class Node:
    def __init__(self,url,prev = None,next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.brow = Node(homepage)
        self.curr = self.brow

    def visit(self, url: str) -> None:        
        temp = Node(url,self.curr,None)
        self.curr.next = temp
        self.curr = temp

    def back(self, steps: int) -> str:
        
        curr = self.curr
        cidx = 0
        while curr.prev and cidx < steps :
            curr = curr.prev
            cidx += 1
        self.curr = curr
        return self.curr.url


    def forward(self, steps: int) -> str:
        curr = self.curr
        cidx = 0
        while curr.next and cidx < steps :
            curr = curr.next
            cidx += 1
        self.curr = curr
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)