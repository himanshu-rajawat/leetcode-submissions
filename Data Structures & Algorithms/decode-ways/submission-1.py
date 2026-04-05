class Solution:
    def numDecodings(self, s: str) -> int:
        # memoization solution
        cache = {}

        def dfs(i):
            if i == len(s):
                return 1
            if i in cache:
                return cache[i]

            res = (dfs(i+1) + (dfs(i+2) if i+1<len(s) and int(s[i:i+2])<=26 else 0)) if s[i]!='0' else 0
            cache[i] = res
            return res

        return dfs(0)

        