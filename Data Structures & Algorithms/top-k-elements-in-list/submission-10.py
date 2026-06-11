class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a dictionary to hold number -> #of times it appears
        numberToFrequencyDict = {}

        # make a list, to be the frequency buckets. #1 bucket holds all numbers that appear once
        # we need len(nums) + 1 buckets. We start counting at 1.
        # index is the frequency
        frequencyBuckets = [[] for i in range(len(nums) + 1)]


        # Go through entire list, filling up our dictionary
        for number in nums:
            numberToFrequencyDict[number] = numberToFrequencyDict.get(number, 0) + 1;

        # go through our dictionary and fill buckets
        for number, frequency in numberToFrequencyDict.items():
            frequencyBuckets[frequency].append(number)

        # iterate from highest frequency bucket downwards, grabbing values and appending to our 
        # list of most common numbers.
        mostCommonNumbers = []

        for i in range(len(frequencyBuckets)-1, 0, -1):
            for number in frequencyBuckets[i]:
                mostCommonNumbers.append(number)

                if len(mostCommonNumbers) == k:
                    return mostCommonNumbers

        return mostCommonNumbers

        # stop returning numbers once we hit k for the size of mostCommonNumsList

