class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # size of the window will be decided by smaller string
        # initialize the window
        l = 0
        counter = {}
        s1_counter = {}
        window_size = len(s1)

        for char in s1:
            s1_counter[char] = s1_counter.get(char, 0)+1

        for r in range(len(s2)):
            # add r pointer
            counter[s2[r]] = counter.get(s2[r], 0)+1
            # shrink window if len(window)>len(s1)
            while r-l+1> window_size:
                counter[s2[l]]-=1
                if counter[s2[l]]==0:
                    del counter[s2[l]]
                l+=1
            if s1_counter == counter:
                return True
        return False
            

