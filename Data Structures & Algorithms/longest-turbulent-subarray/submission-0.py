class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        is_increasing = None



        max_count, curr, prev = 0, 0, None

        for num in arr:
            if prev==None:
                curr+=1
            elif is_increasing == None:
                curr+=1
                if prev<num:
                    is_increasing = True
                elif num<prev:
                    is_increasing = False
                else:
                    curr=1
                    is_increasing = None
            elif is_increasing and prev>num:
                curr+=1
                is_increasing = False
            elif not is_increasing and prev<num:
                curr+=1
                is_increasing = True
            elif prev!=num:
                curr=2
                is_increasing = prev<num
            else:
                curr=1
                is_increasing = None
            
            prev = num
            print(num, curr)
            max_count = max(max_count, curr)
        
        return max_count

            
        