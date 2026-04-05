class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def getFrequencyCount(word):
            counter = {}
            for char in word:
                counter[char] = counter[char]+1 if char in counter else 1
            return counter
        return getFrequencyCount(s) == getFrequencyCount(t)

        