class Solution:
    def lengthOfLastWord(self, s):

        s = s.split()

        if s:

            s = s[-1]
            return len(s)

        else:

            return 0

    def lengthOfLastWord_2(self, s):
        return len(s.rstrip(' ').split(' ')[-1])

def main():
    pass

if __name__ == '__main__':
    main()
    str1 = " Hello World "
    test1 = Solution()
    print(test1.lengthOfLastWord(str1))
    print(test1.lengthOfLastWord_2(str1))


