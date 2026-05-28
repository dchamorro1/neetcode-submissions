class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to hold value -> index pairs
        numsIndexDictionary = {}

        # Add each item in nums to dictionary as well as its index
        for i, n in enumerate(nums):
            complement = target - n

            if complement in numsIndexDictionary:
                return [numsIndexDictionary[complement], i]
        
            numsIndexDictionary[n] = i

        # before adding check to see if x such that x + current = target is found. x = target - current

        # add to dictionary