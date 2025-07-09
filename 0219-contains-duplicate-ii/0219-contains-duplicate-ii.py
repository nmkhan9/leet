class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        visitted = set()
        for i in range (len(nums)) :
            if nums[i] in visitted :
                return True
            visitted.add(nums[i])

            if len(visitted) > k :
                visitted.remove(nums[i-k])
        return False