class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # at each step check to see if its in set. if it is return true
        # add num to set 

        # after loop, return false

        myNums = set()

        for number in nums:
            if number in myNums:
                return True

            myNums.add(number)

        return False

