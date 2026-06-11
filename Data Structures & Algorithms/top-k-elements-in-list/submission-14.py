class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a dictionary: number->frequency
        numToFrequencyDict = {}

        # load up dictionary
        for number in nums:
            numToFrequencyDict[number] = numToFrequencyDict.get(number, 0) + 1

        # make len(nums) + 1 buckets
        frequencyBuckets = [[] for i in range(len(nums) + 1) ]

        # load up buckets (index is frequency)
        for number, frequency in numToFrequencyDict.items():
            frequencyBuckets[frequency].append(number)   

        # count from most full bucket to least full bucket (end to beginning)
        # adding until we reach k amount in our return list
        mostFrequentNums = []

        for bucketIndex in range(len(frequencyBuckets) - 1, 0, -1):
            for bucketNum in frequencyBuckets[bucketIndex]:
                mostFrequentNums.append(bucketNum)

                if (len(mostFrequentNums) == k):
                    return mostFrequentNums

        return mostFrequentNums