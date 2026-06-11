class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # [0,0,0,0,...0] 
        # (count for each 26 letters)

        # compare list of s to that of t

        # OR

        # dictionary approach

        sDictionary = {}

        tDictionary = {}

        for letter in s:
            if letter in sDictionary:
                sDictionary[letter] += 1
            else:
                sDictionary[letter] = 1

        for letter in t:
            if letter in tDictionary:
                tDictionary[letter] += 1
            else:
                tDictionary[letter] = 1

        return sDictionary == tDictionary

        

