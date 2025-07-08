class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        res = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            for p in self.permute(rest):
                res.append([nums[i]] + p)
        return res
            

