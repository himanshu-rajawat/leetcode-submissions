class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        
        def wordMatch(i):
            if i>= len(s):
                return True
            isMatch = False
            n = None
            if i not in cache:
                for dictWord in wordDict:
                    n = len(dictWord)
                    if len(s) > i+n-1 and s[i:i+n] == dictWord:
                        isMatch = wordMatch(i+n)
                    if isMatch:
                        break
                cache[i] = isMatch
            return cache[i]

        return wordMatch(0)
        