class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict of [0, 0, 0 ,, 0] for each letter -> list of words
        letterFrequencyToStrs = defaultdict(list)

        for word in strs:
            letterFrequencyList = [0] * 26
            for letter in word:
                # add to letterFrequencyList
                indexOfLetterInAlphabet = ord(letter) - ord('a')
                letterFrequencyList[indexOfLetterInAlphabet] += 1

            letterFrequencyToStrs[tuple(letterFrequencyList)].append(word)

        return list(letterFrequencyToStrs.values())