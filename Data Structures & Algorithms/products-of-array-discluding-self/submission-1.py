class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # go through array nums and keep a running total of multiplication
        # of all items to left (by reusing what I calulate at each step)

        # input it into result array at each step

        #then do the same starting from the end of the array and multiply what
        # is in results array by that running total

        result = [1] * len(nums)

        prefixMultiplicationTotal = 1
        for i in range(len(nums)):
            result[i] *= prefixMultiplicationTotal
            prefixMultiplicationTotal *= nums[i]

        postFixMultiplicationTotal = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postFixMultiplicationTotal
            postFixMultiplicationTotal *= nums[i]

        return result