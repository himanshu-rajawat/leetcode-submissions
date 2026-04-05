class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""

        for char in s:
            if char.isalnum():
                s1+=char.lower()

        s = s1    
        left, right = 0, len(s)-1    

        while left<=right:
            if s[left]!=s[right]:
                return False
            left, right = left+1, right-1
        return True 
        