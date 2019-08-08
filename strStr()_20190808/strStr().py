class Solution:
    def strStr(self, haystack, needle):

        return haystack.find(needle)

    def strStr_2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

test1 = Solution()

print(test1.strStr("aaaaa","bba"))

print(test1.strStr_2("hello","ll"))