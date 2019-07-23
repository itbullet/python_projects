class Solution:

    def reverse(self, x):

        x_str = str(x)

        if x_str[0:1] == "-":
            x1 = x_str[0:1]
            x2 = x_str[1:]
            x2 = x2[::-1]
            x3 = int(x1+x2)
        else:
            x3 = int(x_str[::-1])

        if x3 >= -2147483648 and x3 <= 	2147483647:
            return x3
        else:
            return 0


test1 = Solution()
x = 120
print(test1.reverse(x))