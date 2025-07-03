class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        dau = -1 if x <0 else 1
        x = abs(x)

        x1 = int(str(x)[::-1])
        
        res = x1*dau

        if res <-2**31 or res >2**31-1 :
            return 0
        else :
            return res