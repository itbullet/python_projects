class Solution:

    def isPalindrome(self, x):

        if x < 0 or (x % 10 == 0 and x != 0):

            return False


        reverted_num = 0
        x_initial = x

        while x>reverted_num:

            pop_num = x % 10
            x //= 10
            reverted_num = reverted_num * 10 + pop_num

        return x == reverted_num or x == reverted_num//10

test1 = Solution()
number = 1214121
print(test1.isPalindrome(number))