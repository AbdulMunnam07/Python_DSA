class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        words = text.split(" ")
        for word in words:
            canType = True
            for ch in word:
                if ch in brokenLetters:
                    canType = False
                    break
            if canType:
                count += 1
        return count


        