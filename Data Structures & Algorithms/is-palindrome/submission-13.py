class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert all chars to lowercase

        # we skip all non alphanumeric characters
        # num < order('a') or num > order(z) skip it
        # same for 0-9
        s = s.lower()

        l = 0
        r = len(s) - 1

        while l <= r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while l < r and not self.isAlphaNumeric(s[r]):
                r -= 1

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

    def isAlphaNumeric(self, myChar):
        return (
        (ord('a') <= ord(myChar) and ord('z') >= ord(myChar))
        or
        (ord('0') <= ord(myChar) and ord('9') >= ord(myChar))
        )





