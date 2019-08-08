class Solution:
    def removeElement(self, nums, val):

        i = 0

        while i < len(nums):

            if nums[i] == val:

                nums.pop(i)
                i -= 1

            i += 1

        return len(nums)

test1 = Solution()
nums = [0,1,2,2,3,0,4,2]
print(test1.removeElement(nums, 2))