class Solution:
    def climbStairs(self, n: int) -> int:
        singleShiftStepCount = 1
        doubleShiftStepCount = 1

        for i in range(n-1):
            temp = singleShiftStepCount

            singleShiftStepCount = singleShiftStepCount + doubleShiftStepCount
            doubleShiftStepCount = temp

        return singleShiftStepCount
