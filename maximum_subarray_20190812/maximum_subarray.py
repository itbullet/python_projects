class Solution:
    def maxSubArray(self, nums):

        sum = nums[0]
        i = 0
        j = 0
        sum_tmp = nums[0]

        for i in range(len(nums)):

            for j in range(i+1, len(nums)):

                sum_tmp += nums[j]

                if sum_tmp > sum:

                    sum = sum_tmp

        return sum

def main():
    pass

if __name__ == '__main__':
    main()

    list1 = [-2, 1, -3, 4, -1, 2, 1, -5 , 4]
    test1 = Solution()
    print(test1.maxSubArray(list1))
