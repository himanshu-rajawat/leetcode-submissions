class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, arr):
            if i>n:
                if len(arr)==k:
                    res.append(arr[:])
                return
            
            arr.append(i)
            backtrack(i+1, arr)
            arr.pop()
            backtrack(i+1, arr)
        backtrack(1, [])
        return res
        