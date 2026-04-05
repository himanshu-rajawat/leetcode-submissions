class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        cand1_count, cand2_count = 0, 0

        for num in nums:
            if cand1==None and num!=cand2:
                cand1 = num
                cand1_count+=1
            elif cand2==None and num!=cand1:
                cand2 = num
                cand2_count+=1
            elif num==cand1:
                cand1_count+=1
            elif num == cand2:
                cand2_count+=1
            else:
                cand1_count-=1
                cand2_count-=1
            
            if cand1 != None and cand2!=None:
                if cand1_count==0:
                    cand1=None
                if cand2_count ==0:
                    cand2=None
            # print(num, cand1, "->", cand1_count, cand2, "->", cand2_count)
        res = set()
        if cand1!=None and nums.count(cand1)>(len(nums)//3):
            res.add(cand1)
        if cand2!=None and nums.count(cand2)>(len(nums)//3):
            res.add(cand2)
        
        return list(res)
        