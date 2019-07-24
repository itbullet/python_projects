import sys

class Solution:

    def reverse(self, x):

        INT_MAX = sys.maxsize

        INT_MIN = -sys.maxsize-1

        x_str = str(x)

        if x_str[0:1] == "-":
            x1 = x_str[0:1]
            x2 = x_str[1:]
            x2 = x2[::-1]
            x3 = int(x1+x2)
        else:
            x3 = int(x_str[::-1])

        if x3 >= INT_MIN and x3 <= INT_MAX:
            return x3
        else:
            return 0

    def reverse_math(self, x):

        INT_MAX = sys.maxsize

        INT_MIN = -sys.maxsize-1

        rev = 0

        while x != 0:

            pop = x % 10
            x //= 10

            if rev > INT_MAX//10 or (rev == INT_MAX//10 and pop > 7):
                return 0
            if rev < INT_MIN//10 or (rev == INT_MIN//10 and pop < -8):
                return 0

            rev = rev * 10 + pop

        return rev

test1 = Solution()
x = 8463847412

print(test1.reverse(x))

print(test1.reverse_math(x))

INT_MAX = sys.maxsize

INT_MIN = -sys.maxsize-1


print("Maximum integer number is {}, minimum integer number is {}.".format(INT_MAX,INT_MIN))