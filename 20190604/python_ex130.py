#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eduar
#
# Created:     04/06/2019
# Copyright:   (c) eduar 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
colors = ["purple", "orange", "green"]

guess = input("Guess color:")

if guess in colors:
    print("You did it!")
else:
    print("You wrong! Try again")