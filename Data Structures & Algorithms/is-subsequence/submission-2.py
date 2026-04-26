class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sIndex = 0
        tIndex = 0

        while(tIndex < len(t) and sIndex < len(s)):
            if(s[sIndex] == t[tIndex]):
                sIndex += 1
            tIndex += 1
        return sIndex == len(s)

        