class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # define a set 
        myNumSet = set()

        for number in nums:
        # check to see if curr num is in set
            if number in myNumSet:
                # if it is return True
                return True
            # if it is not, add it
            myNumSet.add(number)

        return False


        