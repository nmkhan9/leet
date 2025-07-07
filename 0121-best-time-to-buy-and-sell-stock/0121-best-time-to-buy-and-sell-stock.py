class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxsale = 0
        minsale = 10e5

        for price in prices :
            if price < minsale :
                minsale = price
            else :
                maxsale = max(maxsale, price - minsale)
        return maxsale

        