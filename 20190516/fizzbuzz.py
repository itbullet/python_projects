#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eduar
#
# Created:     16/05/2019
# Copyright:   (c) eduar 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
i=1
while i <= 100:
    if (i%3 == 0) and (i%5 == 0):
        print("Fizz Buzz\n")
    elif i%3 == 0:
        print("Fizz\n")
    elif i%5 == 0:
        print ("Buzz\n")
    else:
        print(i,"\n")
    i += 1
