class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedString = ""
        for currString in strs:
            encodedString += str(len(currString)) + "#" + currString

        return encodedString

    def decode(self, s: str) -> List[str]:
        p1 = 0
        decodedStrings = []

        while p1 < len(s):
            p2 = p1

            while s[p2] != "#":
                p2 += 1

            stringLength = int(s[p1:p2])

            p1 = p2 + 1
            p2 = p1 + stringLength

            decodedStrings.append(s[p1:p2])

            p1 = p2
        return decodedStrings

