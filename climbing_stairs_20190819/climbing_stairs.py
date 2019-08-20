import time

start = time.time()

class Solution:
    def climbStairs(self, n):

        if n > 2:

            return self.climbStairs(n-1)+self.climbStairs(n-2)

        elif n == 2:

            return 2

        elif n == 1:

            return 1

        else:

            return 0

    def climbStairs_fast(self, n):

        i = 0
        sum = []

        while i <= n:

            if i == 0:

                sum.append(0)

            elif i == 1:

                sum.append(1)

            elif i == 2:

                sum.append(2)

            else:

                sum.append(sum[i-1]+sum[i-2])

            i += 1

        return sum[i-1]




def main():
    pass

if __name__ == '__main__':
    main()

    test1 = Solution()
    print(test1.climbStairs_fast(28))
    print(test1.climbStairs(28))

end = time.time()

print(end - start)
