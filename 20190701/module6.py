#-------------------------------------------------------------------------------
# Name:        module6
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

#two different ways to itterate through lists

shows = ["breaking bad", "x-files", "fargo"]
coms = ["test1", "test2", "test3"]
all_shows = []

for i, show in enumerate(shows):
    new = shows[i]
    new = new.upper()
    all_shows.append(new)

i = 0
for show in coms:
    all_shows.append(coms[i].upper())
    i += 1


print(all_shows)
