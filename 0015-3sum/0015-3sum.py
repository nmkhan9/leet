class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        nums.sort()
        n = len(nums)
        for i in range(n-2) :
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i+1
            k = n-1
            while j < k :
                total = nums[i] + nums[j] + nums[k]
                if total == 0 :
                    tmp = [nums[i],nums[j],nums[k]]
                    if tmp not in result :
                        result.append(tmp)
                    while j < k and nums[j] == nums[j+1] :
                        j+=1
                    while j < k and nums[k] == nums[k-1] :
                        k-=1
                    j += 1
                    k -=1
                elif total > 0:
                    k -=1
                elif total <0 :
                    j +=1
                    
                
        return result
