#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eduar
#
# Created:     05/06/2019
# Copyright:   (c) eduar 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
my_personal_data = {"height":171, "favorite color":"grey", "favorite actor":"Jason Statham", "weight":72}

answer = input("Please choose height, favorite color, favorite actor or weight")

if answer in my_personal_data:
    print(my_personal_data[answer])
else:
    print("Incorrect choice")