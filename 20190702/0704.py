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

numbers = [11, 21, 33, 69, 77, 99]

while True:

    answer = input("Угадайте число списка или нажмите Х для выхода");

    if answer == "x":
        break

    try:
        answer = int(answer)
    except ValueError:
        print("Введите число либо х")

    if answer in numbers:
        print("Вы угадали число {}.".format(answer))
    else:
        print("Вы не угадали.")
