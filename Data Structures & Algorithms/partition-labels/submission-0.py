class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = {}

        for i in range(len(s)-1, -1, -1):
            if s[i] not in last_occ:
                last_occ[s[i]] = i

        start, parts, end = 0, [], 0

        for j in range(len(s)):
            end = max(last_occ[s[j]], end)
            if end == j:
                parts.append(end-start+1)
                start = end+1
        return parts