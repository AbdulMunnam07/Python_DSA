class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        charWord = {}
        wordChar = {}
        for c, w in zip(pattern, words):
            if c in charWord and charWord[c] != w:
                return False
            if w in wordChar and wordChar[w] != c:
                return False
            charWord[c] = w
            wordChar[w] = c
        return True