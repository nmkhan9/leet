class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        map1 = {}
        map2 = {}
        abc = s.split(" ")
        if len(pattern) != len(abc):
            return False
        for i in range(len(pattern)) :
            if pattern[i] in map1 :
                if map1[pattern[i]] != abc[i] :
                    return False
            else :
                map1[pattern[i]] = abc[i]
            if abc[i] in map2 :
                if map2[abc[i]] != pattern[i] :
                    return False
            else :
                map2[abc[i]] = pattern[i]
        return True
        
        