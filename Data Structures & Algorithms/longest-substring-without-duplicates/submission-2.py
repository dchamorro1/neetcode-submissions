class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep a running total of the maximum length found

        #keep a set to keep the current subString
        charSet = set()

        # set a l pointer at index 0 and r pointer at index 1
        l = 0
        r = 0

        # if new letter at r exists already, increase l
        maxLength = 0

        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            maxLength = max(maxLength, len(charSet))
            r += 1

        return maxLength

