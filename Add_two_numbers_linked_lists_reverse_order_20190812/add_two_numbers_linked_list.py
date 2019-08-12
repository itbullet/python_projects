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

class Solution:

    def addTwoNumbers(self, l1, l2):

        llist_temp = LinkedList()
        str1 = ""
        str2 = ""
        num_tmp = 0

        if not l1 or not l2:

            return l1 or l2

        while l1:
            str1 = str1 + str(l1.data)
            l1 = l1.next

        while l2:
            str2 = str2 + str(l2.data)
            l2 = l2.next

        num_tmp = str(int(str1[::-1])+int(str2[::-1]))[::-1]

        for item in num_tmp:

            llist_temp.addNode(item)



        return llist_temp.head


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

    test1 = Solution()
    llist3.head = test1.addTwoNumbers(llist1.head, llist2.head)
    print("\nResultant list is ")
    print(llist3.printNode())