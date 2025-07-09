class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 :
            return False
        else :
            num = [2,3,5]
            for p in num :
                while n % p == 0 :
                    n = n //p

        return n ==1