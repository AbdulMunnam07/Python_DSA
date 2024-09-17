class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        all_str = s1.split(' ')
        all_str += s2.split(' ')

        counter = Counter(all_str)

        ans = []
        for s, count in counter.items():
            if count == 1:
                ans.append(s)

        return ans