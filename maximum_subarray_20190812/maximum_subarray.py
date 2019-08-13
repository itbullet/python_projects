import time

start = time.time()

class Solution:
    def maxSubArray(self, nums):

        if not nums:

            return None

        if len(nums) == 1:

            return nums[0]

        else:

            sum_tmp = 0
            sum_max = float("-inf")

            for i in nums:

                if sum_tmp<=0:

                    sum_tmp = i

                else:

                    sum_tmp += i

                if sum_tmp > sum_max:

                    sum_max = sum_tmp

            return sum_max

def main():
    pass

if __name__ == '__main__':
    main()

    list1 = [-2,1,-3,4,-1,2,1,-5,4]
    test1 = Solution()
    print(test1.maxSubArray(list1))

end = time.time()

print(end - start)