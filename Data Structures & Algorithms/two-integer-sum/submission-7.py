class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for every number I check all numbers to the right for complement
        # complement = target - num

        numToIndexDictionary = {}


        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numToIndexDictionary:
                return [numToIndexDictionary[complement], i]

            numToIndexDictionary[nums[i]] = i

        return [0,0]
