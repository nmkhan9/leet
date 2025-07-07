class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        visitted = []
        for i in nums:
            if i not in visitted :
                visitted.append(i)
                total += i
            else :
                total -= i

        return total