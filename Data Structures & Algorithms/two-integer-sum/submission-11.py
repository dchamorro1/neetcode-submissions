class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        valToIndex = {}
        # iterate through nums, adding to dictionary value -> index
        # at each stage check dictionary for complement of nummber

        for i, number in enumerate(nums):
            complement = target - number

            if complement in valToIndex:
                return [valToIndex[complement], i]

            valToIndex[number] = i

        return[-1, -1]
