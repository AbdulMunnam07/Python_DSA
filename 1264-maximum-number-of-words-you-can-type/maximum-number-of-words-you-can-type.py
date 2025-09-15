class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Solution no. 1
        # count = 0
        # words = text.split(" ")
        # for word in words:
        #     canType = True
        #     for ch in word:
        #         if ch in brokenLetters:
        #             canType = False
        #             break
        #     if canType:
        #         count += 1
        # return count

        # Solution 2
        broken = set(brokenLetters)
        count = 0
        words = text.split(" ")
        for word in words:
            if all(ch not in broken for ch in word):
                count += 1
        return count


        