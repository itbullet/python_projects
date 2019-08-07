class Solution:
    def removeDuplicates(self, nums):

        id = 0

        while id < len(nums)-1:

            if nums[id] == nums[id+1]:

                nums.pop(id)
                id -= 1

            id += 1

        return len(nums)

test1 = Solution()
l1 = [0,0,1,1,1,2,2,3,3,4]

print(test1.removeDuplicates(l1))
