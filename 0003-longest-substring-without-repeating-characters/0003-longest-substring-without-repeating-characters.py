class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        log = 0
        current = ""

        for c in s:
            if c in current:
                index = current.index(c)
                current = current[index+1:] 
            current += c
            log = max(log, len(current))

        return log
        