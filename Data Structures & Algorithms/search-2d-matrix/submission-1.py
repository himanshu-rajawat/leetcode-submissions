class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        row = None

        while top<=bottom:
            v_mid = top + ((bottom-top)//2)

            if matrix[v_mid][0]>target:
                bottom = v_mid-1
            elif matrix[v_mid][-1]<target:
                top = v_mid+1
            else:
                row = v_mid
                break
        if row==None:
            return False
        
        left, right = 0, len(matrix[row])-1

        while left<=right:
            mid = left+ ((right-left)//2)

            if matrix[row][mid]>target:
                right=mid-1
            elif matrix[row][mid]<target:
                left=mid+1
            else:
                return True
        return False

        