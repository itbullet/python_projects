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
    def mergeTwoLists(self, head1, head2):

    	# create a temp node NULL
    	temp = None

    	# List1 is empty then return List2
    	if head1 is None:
    		return head2

    	# if List2 is empty then return List1
    	if head2 is None:
    		return head1

    	# If List1's data is smaller or
    	# equal to List2's data
    	if head1.data <= head2.data:

    		# assign temp to List1's data
    		temp = head1

    		# Again check List1's data is smaller or equal List2's
    		# data and call mergeLists function.
    		temp.next = self.mergeTwoLists(head1.next, head2)

    	else:
    		# If List2's data is greater than List1's
    		# data assign temp to head2
    		temp = head2

    		# Again check List2's data is greater or equal List's
    		# data and call mergeLists function.
    		temp.next = self.mergeTwoLists(head1, head2.next)

    	# return the temp list.
    	return temp

    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.data < l2.data:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2


llist_1 = LinkedList()
llist_1.addNode(1)
llist_1.addNode(2)
llist_1.addNode(4)

llist_2 = LinkedList()
llist_2.addNode(1)
llist_2.addNode(3)
llist_2.addNode(4)

llist_3 = LinkedList()

test1 = Solution()
llist_3.head = test1.mergeTwoLists(llist_1.head, llist_2.head)
print("\n Merged Linked List is : ", end="")
llist_3.printNode()

llist_1 = LinkedList()
llist_1.addNode(10)
llist_1.addNode(20)
llist_1.addNode(30)
llist_1.addNode(40)
llist_1.addNode(50)

llist_2 = LinkedList()
llist_2.addNode(5)
llist_2.addNode(15)
llist_2.addNode(18)
llist_2.addNode(35)
llist_2.addNode(60)

llist_3 = LinkedList()

test1 = Solution()
llist_3.head = test1.mergeTwoLists2(llist_1.head, llist_2.head)
print("\n Merged Linked List is : ", end="")
llist_3.printNode()








