import os

class Solution:
    def longestCommonPrefix(self, strs):

        lcp = ""
        j = 0

        try:

            j_max = len(min(strs, key = len))

            if len(strs)-1 == 0:

                lcp += strs[0]

            else:

                while j < j_max:

                    ind = False
                    i = 0

                    for i in range(len(strs)-1):
                        if strs[i][j] == strs[i+1][j]:
                            ind = True
                        else:
                            ind = False
                            break

                    if ind == True:
                        lcp += strs[i][j]
                    else:
                        break

                    j += 1

        except ValueError:

            print(lcp)

        return lcp

    def longestCommonPrefix_2(self, strs):

        longest_pre = ""

        if not strs:
            return longest_pre

        shortest_str = min(strs, key = len)

        for i in range(len(shortest_str)):

            if all([x.startswith(shortest_str[:i+1]) for x in strs]):

                longest_pre = shortest_str[:i+1]

            else:

                break

        return longest_pre

    def longestCommonPrefix_3(self, strs):

        if not strs:

            return ""

        shortest_str = min(strs, key = len)

        for i, char in enumerate(shortest_str):

            for other in strs:

                if other[i] != char:

                    return shortest_str[:i]

        return shortest_str

    def longestCommonPrefix_4(self, strs):
        letter_groups, longest_pre = zip(*strs), ""
        # print(letter_groups, longest_pre)
        # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        for letter_group in letter_groups:
            test1 = set(letter_group)
            if len(set(letter_group)) > 1: break
            longest_pre += letter_group[0]
        return longest_pre

    def longestCommonPrefix_5(self, strs):
        def isCommonPrefix(strs, length):
            # has to put 0 in the strs index
            strl = strs[0][:length]
            print(strl)
            for i in range(1,len(strs)):
                if not strs[i].startswith(strl):
                    return False
            return True

        if not strs: return ""
        minLen = len(min(strs, key=len))
        low, high = 1, minLen
        # the binary search on the length of prefix on the first word
        while(low<=high):
            mid = (low+high) // 2
            if (isCommonPrefix(strs, mid)):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:high]



test = Solution()
list1 = ["flower","flow","flight"]

#print(test.longestCommonPrefix(list1))

#print(test.longestCommonPrefix_2(list1))

#print(test.longestCommonPrefix_3(list1))

#print(test.longestCommonPrefix_4(list1))

print(test.longestCommonPrefix_5(list1))

#print(os.path.commonprefix(list1))
