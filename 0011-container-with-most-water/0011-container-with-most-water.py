class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = -9999
        left = 0
        right = len(height) - 1
        while left < right :
            cd = right - left
            cr = min(height[left], height[right])
            dt = cd*cr
            s = max(dt, s)
            if height[left] < height[right] :
                left += 1
            else :
                right -=1
        return s
