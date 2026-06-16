class Solution:
    def climbStairs(self, n: int) -> int:
        singleShiftStepCount = 1
        doubleShiftStepCount = 1

        totalSum = 0

        for i in range(n-1):
            totalSum = singleShiftStepCount + doubleShiftStepCount

            temp = singleShiftStepCount

            singleShiftStepCount = totalSum
            doubleShiftStepCount = temp

        return singleShiftStepCount
