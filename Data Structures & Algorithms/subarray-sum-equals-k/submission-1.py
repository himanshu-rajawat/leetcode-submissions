class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        s=0
        res = 0
        for i in range(len(nums)):
            num = nums[i]
            s+=num
            if (s-k) in prefix_sum:
                res+=prefix_sum[s-k]
            prefix_sum[s] = prefix_sum.get(s,0)+1
        return res