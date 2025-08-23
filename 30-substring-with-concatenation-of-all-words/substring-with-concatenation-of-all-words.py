class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        total = len(words) * l

        wordsDict = Counter(words)
        result = []

        for start in range(0, len(s) - total + 1):
            
            sWords = [s[i:i + l] for i in range(start, start + total, l)]
            if Counter(sWords) == wordsDict:
                result.append(start)

        return result
