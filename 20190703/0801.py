#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eduar
#
# Created:     03/07/2019
# Copyright:   (c) eduar 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import statistics

nums = [1, 5, 12, 14, 33, 46, 33, 2]
shares = [2.5, 3, 10]

print(statistics.median_high(nums))

print(statistics.median_low(nums))

print(statistics.harmonic_mean(nums))

print(statistics.median_grouped(nums))