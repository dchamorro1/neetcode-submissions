class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort nums - because that allows O(N) time
        nums.sort()

        # Make results array
        results = []

        # Go through Nums and enumerate it
            # for each iteration, set left pointer to be 1 more than a (which starts at 0)
            # set r to be at the end
            # if we get to a being 0 we break
            # if current i, l, or r, is the same as previous i, l , r, we skip it. 
            #   This means add 1 to l, subtract 1 from r, or just continue for i
            #    This helps avoid duplicate sets of 3 in result
            #   Different pointers can have the same value but we don't want the same pointer processing same value twice

        for i, currentValue in enumerate(nums):
            if currentValue > 0:
                break
            
            # skip currentValue from processing same value twice
            if i > 0 and currentValue == nums[i - 1]:
                continue

            leftPointer = i+1
            rightPointer = len(nums) - 1

            while leftPointer < rightPointer:
                totalThreeSum = currentValue + nums[leftPointer] + nums[rightPointer]

                if totalThreeSum > 0:
                    rightPointer -= 1
                elif totalThreeSum < 0:
                    leftPointer += 1
                else:
                    results.append([currentValue, nums[leftPointer], nums[rightPointer]])
                    leftPointer += 1
                    rightPointer -= 1

                    while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer - 1]:
                        leftPointer+= 1

                    while leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer + 1]:
                        rightPointer-= 1

        return results

        