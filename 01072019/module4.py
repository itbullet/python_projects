#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      eduar
#
# Created:     01/07/2019
# Copyright:   (c) eduar 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
tv = ["Breaking Bad",
        "X-files",
        "Fargo"]

i=0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)
