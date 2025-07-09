class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) :
            return False
        else :
            map1 = {}
            map2 = {}
            n = len(s)
            for i in range(n) :
                if s[i] in map1 :
                    if map1[s[i]] != t[i] :
                        return False
                else :
                    map1[s[i]] = t[i]
                
                if t[i] in map2 :
                    if map2[t[i]] != s[i] :
                        return False
                else :
                    map2[t[i]] = s[i]
        return True