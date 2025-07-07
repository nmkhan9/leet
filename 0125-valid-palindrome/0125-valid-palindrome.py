class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [x.lower() for x in s if x.isalnum()]
        return s == s[::-1]