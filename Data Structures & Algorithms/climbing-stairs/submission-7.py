class Solution:
    def climbStairs(self, n: int) -> int:
        doubleShiftStepCount = 1
        singleShiftStepCount = 1

        # if n = 3, we need to calcualte
        # ways to get to 0, 1, 2, 3
        # we already know ways to get to 0, and 1

        # n will be 0 and 1 which is 2 times
        # this gives us ways to get to 2 and 3 that we are missing

        for i in range(n-1):
            temp = singleShiftStepCount

            singleShiftStepCount = doubleShiftStepCount + singleShiftStepCount 
            doubleShiftStepCount = temp

        return singleShiftStepCount

        # Time: O(n)
        # Space: O(1)
