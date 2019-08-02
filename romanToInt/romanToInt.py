class Solution:
    def romanToInt(self, s):

        roman = {"I" : 1, "IV" : 4, "V" : 5, "IX" : 9, "X" : 10, "XL" : 40, "L" : 50, "XC" : 90, "C" : 100, "CD" : 400, "D" : 500, "CM" : 900, "M" : 1000}
        num = 0
        size = len(s)
        i = 0

        while i < size:

            if i < size-1:

                if s[i] == "C" and s[i+1] == "M":
                    num += roman["CM"]
                    i += 1
                elif s[i] == "C" and s[i+1] == "D":
                    num += roman["CD"]
                    i += 1
                elif s[i] == "X" and s[i+1] == "C":
                    num += roman["XC"]
                    i += 1
                elif s[i] == "X" and s[i+1] == "L":
                    num += roman["XL"]
                    i += 1
                elif s[i] == "I" and s[i+1] == "X":
                    num += roman["IX"]
                    i += 1
                elif s[i] == "I" and s[i+1] == "V":
                    num += roman["IV"]
                    i += 1
                else:
                    num += roman[s[i]]
            else:
                num += roman[s[i]]
            i +=1

        return num

test = Solution()

print(test.romanToInt("XXVII"))
