class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # do a sliding window on s2 and for any window if count maps are equal for s1 and s2 return true else false

        # create count map for s1
        s1_char_count = {}
        for char in s1:
            s1_char_count[char]=s1_char_count.get(char,0)+1

        # sliding window on s2
        s2_win_char_count = {}
        n = len(s2)

        for i in range(n):
            char = s2[i]
            s2_win_char_count[char] = s2_win_char_count.get(char,0)+1

            # removing extra chars from window
            if i >= len(s1):
                del_char = s2[i-len(s1)]
                s2_win_char_count[del_char]-=1

                if s2_win_char_count[del_char]==0:
                    del s2_win_char_count[del_char]

            # compare each window count with s1
            if s2_win_char_count == s1_char_count:
                return True
        return False

        