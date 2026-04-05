class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word))+'#'+word
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        flag = True and len(s)>0
        i = 0
        words = []
        while flag:
            print(i)
            word_len = ''
            while i<len(s) and s[i]!="#":
                word_len += s[i]
                i+=1
            word_len = int(word_len)
            words.append(s[i+1:i+word_len+1])
            i = i+word_len+1
            if(i>=len(s)):
                flag = False
        return words
        

