class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        import numpy as np
        if n == 0 or n == 1 :
            return 1
        abc = np.zeros(n+1)
        abc[0] = 1
        abc[1] = 1
        for i in range(2,n+1):
            abc[i] = abc[i-1] +abc[i-2]
        return int(abc[n])
        
        