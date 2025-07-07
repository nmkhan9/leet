class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        hjhj = None
        for num in nums :
            if cnt == 0 :
                hjhj = num
            cnt +=1 if num==hjhj else -1
        return hjhj