class Solution:
    def uniqueOccurrences(selarr):
        dict = {}

        for i in range(len(arr)):
            dict[arr[i]] = 1 + dict.get(arr[i], 0)

        return len(dict) == len(set(dict.values()))
        