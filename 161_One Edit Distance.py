class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # faster with shorter slicing
        if abs(len(s)-len(t))>1 or s == t: return False
        if len(s)-len(t) == -1:
            for i in range(len(s)):
                if s[i]!=t[i]: return s[i:] == t[i+1:]
        elif len(s)-len(t) == 1:
            for i in range(len(t)):
                if s[i]!=t[i]: return t[i:] == s[i+1:]
        else:
            for i in range(len(t)):
                if s[i]!=t[i]: return t[i+1:] == s[i+1:]
        return True
        
        # if abs(len(s)-len(t))>1: return False
        # if len(s)-len(t) == -1:
        #     return True if any(t[:i]+t[i+1:] == s for i in range(len(t))) else False
        # elif len(s)-len(t) == 1:
        #     return True if any(s[:i]+s[i+1:] == t for i in range(len(s))) else False
        # else:
        #     # for i in range(len(s)):
        #     #     if s[i] != t[i]: return s[i+1:] == t[i+1:]
        #     # return False
        #     count = sum(s[i] != t[i] for i in range(len(s)))
        #     return True if count == 1 else False
                
