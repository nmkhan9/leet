class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visitted = []
        ls = []
        for i in nums :
            if i not in visitted :
                visitted.append(i)
            else :
                ls.append(i)
        abc = [x for x in visitted if x not in ls]
        return abc[0]