class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs:
            if s =="":
                return s
            for i in range(len(prefix)):
                if i>=len(s) or s[i]!=prefix[i]:
                    prefix = prefix[:i]
                    print(s, prefix)
                    break
        return prefix