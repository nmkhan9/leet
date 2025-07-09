class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 :
            return False

        import math

        num = math.log(n,3)
        return abs(num - round(num)) < 1e-10
        