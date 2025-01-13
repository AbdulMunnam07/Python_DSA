class Solution:
    def minimumLength(self, s: str) -> int:
        dictionary = Counter(s)

        delete_count = 0

        for i in dictionary.values():
            if i % 2 == 1:
                delete_count += i - 1
            else:
                delete_count += i - 2

        return len(s) - delete_count