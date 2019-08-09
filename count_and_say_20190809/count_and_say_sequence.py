class Solution:
    def countAndSay(self, n):

        num_str = "1"
        tmp_str = ""
        level = 1

        if n == 0:

            return 0


        while level < n:

            print(num_str)
            str_len = len(num_str)
            i = 0
            j = 0

            while i < str_len:

                char = num_str[i]
                count = 0

                while j < str_len:

                    if num_str[j] == char:

                        count += 1
                        j += 1

                    else:

                        break

                tmp_str = tmp_str+str(count)+char

                i = j

            num_str = tmp_str
            tmp_str = ""
            level += 1

        return num_str

##########

def main():
    pass

if __name__ == '__main__':
    main()

    test1 = Solution()
    run_program = ""

    while run_program != "x":

        try:

            number = int(input("\nEnter a number n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence: "))
            print(test1.countAndSay(number))
            run_program = input("\nPress x if you want to close the program: ")

        except:

            print("You entered not a number!")
            run_program = input("\nPress x if you want to close the program: ")


