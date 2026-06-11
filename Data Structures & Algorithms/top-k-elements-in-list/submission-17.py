class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        letterToFrequencyDict = {}

        # fill a dictionary of number -> count
        for number in nums:
            letterToFrequencyDict[number] = letterToFrequencyDict.get(number, 0) + 1

        # make a list where index represents frequency of length nums + 1
        indexAsFrequencyBuckets = [[] for _ in range(len(nums) + 1)]

        # list where the k most frequent elements are at end
        for number, frequency in letterToFrequencyDict.items():
            indexAsFrequencyBuckets[frequency].append(number)

        mostFrequentNums = []

        # then we iterate from end of list k times 
        for i in range(len(indexAsFrequencyBuckets) - 1, 0, -1):
            for number in indexAsFrequencyBuckets[i]:
                mostFrequentNums.append(number)

                if len(mostFrequentNums) == k:
                    return mostFrequentNums

        return mostFrequentNums