class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # idea is to build a sliding window of dynamic size starting from 1st element
        def is_valid(char_count):
            return sum(char_count.values())-max(char_count.values())<=k
        n, max_len, left_idx = len(s), 0, 0
        char_count = {}

        # sliding window
        for i in range(n):
            char = s[i]
            # update char count
            char_count[char]=char_count.get(char,0)+1

            # check if valid string
            valid = is_valid(char_count)
            if valid:
                # compare and set max length
                max_len = max(max_len, sum(char_count.values()))
            else:
                # keep removing chars while string is not valid
                while not valid:
                    char_count[s[left_idx]]-=1
                    left_idx+=1
                    valid = is_valid(char_count)

        return max_len
        