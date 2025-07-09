class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mapp = {}
        for i in range (len(s)) :
            if s[i] not in mapp :
                mapp[s[i]] = 1
            else : 
                mapp[s[i]] += 1

        for i in range (len(t)) :
            if t[i] in mapp and mapp[t[i]] > 0 :
                mapp[t[i]] -= 1
            else :
                return t[i]
