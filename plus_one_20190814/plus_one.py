class Solution:
    def plusOne(self, digits):

        s = ""

        for i in digits:
            s = s + str(i)

        return list(map(int, str(int(s)+1)))

    def plusOne2(self, digits):

        s = ""

        for i in digits:
            s = s + str(i)

        s = int(s) + 1

        return [int(x) for x in str(s)]

def main():
    pass

if __name__ == '__main__':
    main()

    test1 = Solution()
    list1 = [2, 0, 1 , 9]
    print(test1.plusOne(list1))
    print(test1.plusOne2(list1))