class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # trying a backtracking solution
        res = []
        def backtrack(curr_str,open_num, close_num):
            if open_num>0:
                backtrack(curr_str+"(", open_num-1, close_num)
            if close_num>0 and open_num<close_num:
                backtrack(curr_str+")", open_num, close_num-1)
            if open_num==0 and close_num==0:
                res.append(curr_str)
        backtrack("",n,n)
        return res

        