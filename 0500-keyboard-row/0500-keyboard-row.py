class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        res = []
        for word in words:
            lower_set = set(word.lower())
            if lower_set.issubset(row1) or lower_set.issubset(row2) or lower_set.issubset(row3) :
                res.append(word)
        return res