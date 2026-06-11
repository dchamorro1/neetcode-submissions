class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary of letter counts [0,0,0...0] for 26 letters 
        #->
        # list of strings that match

        # then go through all values in dictionary and add them to a anagrams list

        charCountsToStrings = defaultdict(list)

        # fill up dictionary

        for word in strs:
            currLetterCountList = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                currLetterCountList[index] += 1

            charCountsToStrings[tuple(currLetterCountList)].append(word)

        anagramsResult = []

        for letterCountsList, words in charCountsToStrings.items():
            # anagramsResult.addRange(words)
            anagramsResult.append(words)

        return anagramsResult


