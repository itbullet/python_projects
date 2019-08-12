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

    def addTwoNumbers(self, l1, l2):

        prev = None
        temp = LinkedList()
        carry = 0

        while l1 is not None or l2 is not None:

            a = 0 if l1 is None else l1.data

            b = 0 if l2 is None else l2.data

            sum = carry + a + b

            carry = (a + b) // 10

            if sum < 10:

                sum = sum

            else:

                sum %= 10

            temp.addNode(sum)

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            temp.addNode(carry)

        return temp


def main():
    pass

if __name__ == '__main__':
    main()

    llist1 = LinkedList()
    llist1.addNode(2)
    llist1.addNode(4)
    llist1.addNode(3)
    print("First List is ")
    llist1.printNode()

    llist2 = LinkedList()
    llist2.addNode(5)
    llist2.addNode(6)
    llist2.addNode(4)
    print("\nSecond List is ")
    llist2.printNode()

    llist3 = LinkedList()

    llist3 = llist3.addTwoNumbers(llist1.head, llist2.head)
    print("\nResultant list is ")
    print(llist3.printNode())