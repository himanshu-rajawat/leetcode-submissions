class Solution:
    def __init__(self):
        self.cache = {}
    def uniquePaths(self, m: int, n: int) -> int:
        return int(self.fact(m+n-2)/(self.fact(m-1)*self.fact(n-1)))

    def fact(self, n):
        if n == 0 or n == 1:
            return 1
        if n not in self.cache:
            self.cache[n] = n*self.fact(n-1)
        return self.cache[n]
        