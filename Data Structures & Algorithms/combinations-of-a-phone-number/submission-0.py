class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}
        res = []
        def backtrack(nums, combination):
            if nums=="":
                if combination!="":
                    res.append(combination[:])
                return
            
            for char in mapping[nums[0]]:
                combination+=char
                backtrack(nums[1:], combination)
                combination = combination[:-1]
        backtrack(digits, "")
        return res
        