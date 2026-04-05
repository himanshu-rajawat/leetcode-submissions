class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        idx = 0
        print(s)
        res = []
        while idx<len(s):
            word_len = ""
            while idx<len(s) and s[idx]!='#':
                word_len+=s[idx]
                idx+=1
            word_len = int(word_len)
            res.append(s[idx+1:idx+word_len+1])
            idx = idx+word_len+1
        return res
