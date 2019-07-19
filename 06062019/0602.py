#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eduard
#
# Created:     06.06.2019
# Copyright:   (c) Eduard 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

word1 = input("Enter first word")

word2 = input("Enter second word")

str = "Yesterday I wrote {}. Yesterday I went to {}.".format(word1, word2)

print(str)