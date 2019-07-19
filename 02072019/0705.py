#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eduar
#
# Created:     02/07/2019
# Copyright:   (c) eduar 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
common_list = []

for i in list1:

    for j in list2:
        common_list.append(i*j)

print(common_list)