class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ls = sorted(nums1 + nums2)
        n = len(ls)
        if n % 2 == 1 :
            return float(ls[n//2])
        else :
            return float((ls[n//2-1]+ls[n//2])/2.0)

        