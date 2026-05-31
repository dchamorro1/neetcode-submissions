class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # stat with a left and right pointer at each extreme

        # calculate area using these 2 pointers

        # set result = to the area found with those pointers

        # decide whether to increase l or decrease r based on which is shorter of the two (taking best possible path and leaving other one)
        # we iterate on the shorter one

        l = 0
        r = len(heights) - 1

        maximumArea = 0

        while l < r:
            differenceBetweenLAndR = r - l
            areaCalculated = differenceBetweenLAndR * min(heights[l], heights[r])

            maximumArea = max(maximumArea, areaCalculated)

            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1

        return maximumArea

