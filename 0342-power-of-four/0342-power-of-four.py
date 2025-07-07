class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if n <= 0 :
            return False

        abc = math.log(n, 4)
        if abc == int(abc) :
            return True
        else :
            return False 
        