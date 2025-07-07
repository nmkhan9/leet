class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        char = strs[0]
        for i in strs[1:] :
            while not i.startswith(char) :
                char = char[:-1]
                if not char :
                    return ""
        return char
        