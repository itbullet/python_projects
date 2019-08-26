class Solution:

    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
        print(nums1)

def main():
    pass

if __name__ == '__main__':
    main()

    test1 = Solution()
    nums_A = [-1,0,0,1,0,0]
    m = 4
    nums_B = [2,5,6,0]
    n = 3
    test1.merge(nums_A, m, nums_B, n)
