class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        Set = set()

        for i in range(len(sentence)):
            Set.add(sentence[i])

        if len(Set) == 26:
            return True

        else:
            False
        