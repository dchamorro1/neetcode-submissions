class Solution:
    def isValid(self, s: str) -> bool:
        charStack = []
        closeToOpenDictionary = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        # iterate over each char in s
        for currChar in s:
            if charStack and currChar in closeToOpenDictionary and charStack[-1] == closeToOpenDictionary[currChar]:
                charStack.pop()
            else:
                charStack.append(currChar)

        if charStack == []:
            return True
        else:
            return False