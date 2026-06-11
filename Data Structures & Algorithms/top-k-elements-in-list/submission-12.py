class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a dictionary of number -> frequency
        numToFrequencyDict = {}

        # make a list of list with len(nums) + 1 buckets
        # index represents frequency
        frequencyBuckets = []
        for i in range(len(nums) + 1):
            frequencyBuckets.append([])

        # OR
        # frequencyBuckets = [[] for i in range(len(nums) + 1)]

        # fill up dictionary
        for number in nums:
            numToFrequencyDict[number] = numToFrequencyDict.get(number, 0) + 1

        # fill up our buckets with dictionary
        for number, frequency in numToFrequencyDict.items():
            frequencyBuckets[frequency].append(number)

        mostFrequentNums = []

        # go from largest to lowest frequency bucket (end to beginning)
        # adding numbers to result array until we have k numbers
        for i in range(len(nums), 0, -1):
            for bucketNum in frequencyBuckets[i]:
                mostFrequentNums.append(bucketNum)

                if (len(mostFrequentNums) == k):
                    return mostFrequentNums

        return mostFrequentNums

