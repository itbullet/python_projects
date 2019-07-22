#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eduar
#
# Created:     27/05/2019
# Copyright:   (c) eduar 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

age = input()

if age == "25":
    print ("You are twenty five")
elif int(age) < 18:
    print ("You are too young")
elif age == "33":
    print ("Jesus age ;-)")
elif age == "36":
    print ("Same age like me")
else:
    print ("Others...")