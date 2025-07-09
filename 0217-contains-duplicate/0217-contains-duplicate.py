class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ls = list(set(nums))
        if len(ls) != len(nums):
            return True
        else :
            return False
        