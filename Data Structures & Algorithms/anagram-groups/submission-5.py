class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Make a dictionary of a list of counts where each index corresponds 
        # to the corresponding index of that letter in the alphabet

        # Then as value for the dictionary, make it a list of all the words that follow that count

        # 1. Go through each word in strs and add it as value in dictionary and pass it in as a tuple in the value

        letterCountsToListDict = defaultdict(list)
        for word in strs:
            letterCounts = [0] * 26
            for letter in word:
                letterAlphabetIndex = ord(letter) - ord('a')
                letterCounts[letterAlphabetIndex] += 1
            
            letterCountsToListDict[tuple(letterCounts)].append(word)

        return list(letterCountsToListDict.values())



        