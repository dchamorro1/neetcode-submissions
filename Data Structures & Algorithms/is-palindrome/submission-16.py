class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert s to lowercase
        s = s.lower()

        # make l pointer and r pointer
        l = 0
        r = len(s) - 1

        while l <= r:
            # while l not valid iterate it (same for r)
            # use isalnum() to make sure its alpha numeric

            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l] != s[r]:
                return False
            else:
            # incremenet l and r
                l += 1
                r -= 1
        
        return True

        