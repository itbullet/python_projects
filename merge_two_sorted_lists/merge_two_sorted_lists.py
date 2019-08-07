class Solution:
    def mergeTwoLists(self, l1, l2):

        l3 = []

        while l1 or l2:
        	if len(l1)>0:
        		if l1[0] <= l2[0]:
        			l3.append(l1.pop(0))
        		elif len(l2)>0:
        			l3.append(l2.pop(0))
        	elif len(l2)>0:
        		l3.append(l2.pop(0))


        return l3


l1 = [1, 2, 4]

l2 = [1, 3, 4]

l1.sort()

l2.sort()

test1 = Solution()

print(test1.mergeTwoLists(l1, l2))