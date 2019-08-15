class Solution:
    def addBinary2(self, a, b):

        return bin(int(a,2)+int(b,2))[2:]

    def addBinary(self, a, b, i):

            i += 1

            print("round: ",i)
            print("a: ",a)
            print("b: ",b)

            if len(a)==0:
                return b
            if len(b)==0:
                return a
            if a[-1] == '1' and b[-1] == '1':
                return self.addBinary(self.addBinary(a[0:-1],b[0:-1], i),'1', i)+'0'
            if a[-1] == '0' and b[-1] == '0':
                return self.addBinary(a[0:-1],b[0:-1], i)+'0'
            else:
                return self.addBinary(a[0:-1],b[0:-1], i)+'1'


def main():
    pass

if __name__ == '__main__':
    main()

    test1 = Solution()
    num1 = "1010"
    num2 = "1011"
    i = 0
    #print(test1.addBinary2(num1, num2))
    print(test1.addBinary(num1, num2, i))
