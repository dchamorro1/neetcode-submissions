class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Compare lengths. If not equal, return false
        if len(s) != len(t):
            return False

        # Build Hash Maps for both strings. Key: Letter, Value: Frequency
        sDict = {}
        tDict = {}

        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i], 0) + 1
            tDict[t[i]] = tDict.get(t[i], 0) + 1

        # Compare HashMaps (should be identical). If so, return true
        return sDict == tDict
