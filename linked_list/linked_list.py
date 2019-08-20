class ListNode:
    def __init__(self,data):
       self.data = data
       self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printNode(self):
        curr = self.head
        while curr:
           print(curr.data, end="->")
           curr = curr.next

    def addNode(self,data):
        newNode = ListNode(data)

        if self.head is None:
            self.head = newNode
            return
        last = self.head

        while last.next:
            last = last.next
        last.next = newNode