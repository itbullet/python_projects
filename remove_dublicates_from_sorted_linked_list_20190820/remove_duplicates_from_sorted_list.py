import sys
sys.path.append(r"..\linked_list")

import linked_list

class Solution:
    def deleteDuplicates(self, head):

        curr = head
        test = head

        while (curr is not None):

            temp = curr.next

            if temp == None:

                break

            else:

                if curr.data == temp.data:
                    curr.next = temp.next
                    temp = curr.next


                if temp == None:
                    break

                if curr.data != temp.data:

                    curr = curr.next

                else:

                    curr = curr

        return test


def main():
    pass

if __name__ == '__main__':
    main()

    llist1 = linked_list.LinkedList()
    llist1.addNode(1)
    llist1.addNode(1)
    llist1.addNode(1)
    llist1.addNode(3)
    llist1.addNode(3)
    print("Linked list is ")
    llist1.printNode()

    llist3 = linked_list.LinkedList()

    test1 = Solution()
    llist3.head = test1.deleteDuplicates(llist1.head)
    print("\nResultant linked list whithout duplicates is ")
    print(llist3.printNode())