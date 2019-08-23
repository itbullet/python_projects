class Solution:
    def merge(self, nums1, m, nums2, n):

        temp = 0
        j = 0

        if n != 0:

            for i in range(m+n):

                tmp1 = nums2[j]

                if i<len(nums1):
                    tmp2 = nums1[i]

                    if nums2[j] <= nums1[i]:

                        nums1.insert(i, nums2[j])
                        j += 1

                else:

                    nums1.insert(i, nums2[j])
                    j += 1


        print(nums1)



def main():
    pass

if __name__ == '__main__':
    main()

    test1 = Solution()
    nums_A = [1]
    m = len(nums_A)
    nums_B = []
    n = len(nums_B)
    test1.merge(nums_A, m, nums_B, n)
