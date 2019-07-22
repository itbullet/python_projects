#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eduard
#
# Created:     29.05.2019
# Copyright:   (c) Eduard 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def fun6(x):
    """
    :converts variable string x to float number
    :if x is not a number then exception
    """
    try:
        return float(x)
    except ValueError:
        print("Wrong format of variable")

y = input()

print(fun6(y))