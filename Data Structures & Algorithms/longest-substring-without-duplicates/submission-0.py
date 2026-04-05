class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start with window of size 1 and keep increasing until we have unique elements, drop if we have duplicate

        last_seen = {}
        curr, max_len, valid_idx = 0, 0, 0

        while curr<len(s):
            if s[curr] in last_seen and last_seen[s[curr]]>=valid_idx:
                max_len = max(max_len, curr-last_seen[s[curr]])
                valid_idx = last_seen[s[curr]]+1
                last_seen[s[curr]] = curr
            else:
                last_seen[s[curr]] = curr
                max_len = max(max_len, curr-valid_idx+1)
            curr+=1

        return max_len
            
        