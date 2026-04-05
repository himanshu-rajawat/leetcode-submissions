class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force solution is n^3
        #optimised solution we will have three pointers, one will just iterate over the list and rest two will be like a two sum problem
    
        #sort the list
        nums.sort() 
        output_list = []
        prev = None

        #iterate over the list
        for i in range(len(nums)):
            target = - nums[i]
            start, end = i+1, len(nums)-1 
            while start<end<len(nums) and nums[i]!=prev :
                curr_sum = nums[start]+nums[end]
                if (curr_sum==target):
                    output_list.append([nums[i], nums[start], nums[end]])
                    flag1 = True
                    while start<end and flag1:
                        flag1 = nums[start]==nums[start+1] if start+1<end else False
                        start+=1
                elif (curr_sum>target):
                    end-=1
                else:
                    start+=1
            prev = nums[i]

        
        return output_list

        