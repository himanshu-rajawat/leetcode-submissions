class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # do not use an element once you skip it
        res = []
        candidates.sort()
        def backtrack(i, currSet, currSum, lastSkipped):
            if currSum==target:
                res.append(currSet)
                return
            if i >= len(candidates) or currSum>target:
                return
            curr = candidates[i]

            # include next element only when it is different than last element, in case last element was skipped
            if not (lastSkipped and lastSkipped==curr):
                backtrack(i+1, currSet+[curr],currSum+curr, None) #include current element

            backtrack(i+1, currSet, currSum, curr) #skip current ele

        backtrack(0,[],0,None)
        return res
        
        