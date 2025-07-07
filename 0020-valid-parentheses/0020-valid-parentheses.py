class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for i in s :
            if i in mapping :
                if not stack or stack[-1] != mapping[i]:
                    return False
                stack.pop()
            else :
                stack.append(i)
        return not stack

        