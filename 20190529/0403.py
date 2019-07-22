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

def fun3(x, y, z, a=2, b=3):
    #returns sum of  variables
    return  x+y+z+a+b

print(fun3(1,2,3,10))