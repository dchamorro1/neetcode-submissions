class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert to all lowercase
        s = s.lower()

        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            # skip the non alpha numerics
            while p1 < p2 and not s[p1].isalnum():
                p1 += 1
            while p1 < p2 and not s[p2].isalnum():
                p2 -=1

            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        
        return True


