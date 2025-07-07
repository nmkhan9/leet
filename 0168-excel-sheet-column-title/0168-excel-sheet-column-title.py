class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        mapp = {i: chr(64 + i) for i in range(1, 27)}
        result = ""

        while columnNumber > 0:
            mod = columnNumber % 26
            if mod == 0:
                result = mapp[26] + result
                columnNumber = columnNumber // 26 - 1
            else:
                result = mapp[mod] + result
                columnNumber = columnNumber // 26

        return result