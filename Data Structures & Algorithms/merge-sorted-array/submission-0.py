class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, curr = len(nums1)-len(nums2)-1, len(nums2)-1, len(nums1)-1
        while curr>=0:
            if p1>=0 and p2>=0:
                if nums1[p1]>nums2[p2]:
                    nums1[curr]=nums1[p1]
                    p1-=1
                else:
                    nums1[curr]=nums2[p2]
                    p2-=1
            elif p1>=0:
                nums1[curr]=nums1[p1]
                p1-=1
            else:
                nums1[curr]=nums2[p2]
                p2-=1 
            curr-=1 