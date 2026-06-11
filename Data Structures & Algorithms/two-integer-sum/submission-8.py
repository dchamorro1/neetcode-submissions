class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary with value to index
        valueToIndex = {}

        # for each number we check to see if the complement is in our dict,
        # if it is we return the indexes of both
        for i, number in enumerate(nums):
            complement = target - number

            if complement in valueToIndex:
                return [valueToIndex[complement], i]

            valueToIndex[number] = i

        return [-1,-1]

