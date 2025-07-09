class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if n <= 0:
            return False
        num = math.log(n,2)
        return abs(num - round(num)) < 1e-10
        