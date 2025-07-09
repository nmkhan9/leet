class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapp = {}
        if len(s) != len(t) :
            return False
        else :
            for i in range (len(s)) :
                if s[i] not in mapp :
                    mapp[s[i]] = 1
                else :
                    mapp[s[i]] +=1
            for i in range (len(t)) :
                if t[i] not in mapp or mapp[t[i]] == 0 :
                    return False
                mapp[t[i]] -= 1
        return True