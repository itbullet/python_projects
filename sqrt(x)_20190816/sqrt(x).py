import math

class Solution:
    def mySqrt(self, x):

        return int(math.sqrt(x))

def mySqrt(self, x):
    if x < 2:
        return x

    left, right = 2, x // 2

    while left <= right:
        pivot = left + (right - left) // 2
        num = pivot * pivot
        if num > x:
            right = pivot -1
        elif num < x:
            left = pivot + 1
        else:
           return pivot

    return right


def main():
    pass

if __name__ == '__main__':
    main()

    test1 = Solution()
    print(test1.mySqrt(8))
    print(test1.mySqrt(16))