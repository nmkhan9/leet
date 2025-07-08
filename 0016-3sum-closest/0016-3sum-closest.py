class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        tmp = float
        result = 0

        for i in range(n) :
            j,k = i+1,n-1
            while j < k :
                total = nums[i] + nums[j] +nums[k]
                hjhj = abs(total - target)
                if hjhj < tmp :
                    tmp = hjhj
                    result = total
                if total == target :
                    return target
                elif total < target :
                    j+=1
                else :
                    k-=1
        return result

        