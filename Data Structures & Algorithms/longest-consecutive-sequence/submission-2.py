class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestSequence = 0

        for num in nums:
            currentLength = 1
            if num - 1 not in numsSet:
                while num + currentLength in numsSet:
                    currentLength += 1
                longestSequence = max(longestSequence, currentLength)

        return longestSequence