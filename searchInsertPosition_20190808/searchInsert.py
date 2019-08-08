class Solution:
    def searchInsert(self, nums, target):

        for id,item in enumerate(nums):

            if item == target:

                return id

            elif target > item:

                pass

            else:

                return id

        return len(nums)

    def searchInsert_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        print([x for x in nums if x<target])
        return len([x for x in nums if x<target])

    def searchInsert_binary(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

test1 = Solution()
nums = [1,3,5,6]
print(test1.searchInsert_binary(nums, 0))