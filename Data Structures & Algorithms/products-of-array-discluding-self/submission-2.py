class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make list of size nums with all 1s to be able to *= from beginning
        multipliedExceptSelf = [1] * len(nums)

        # left pass where each num is equal to all the nums that came before it
        runningLeftProduct = 1
        for i, number in enumerate(nums):
            multipliedExceptSelf[i] *= runningLeftProduct
            runningLeftProduct *= number

        # then do a right pass and multiply existing values in result array by all values from nums that came before it
        runningRightProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            multipliedExceptSelf[i] *= runningRightProduct
            runningRightProduct *= nums[i]

        return multipliedExceptSelf