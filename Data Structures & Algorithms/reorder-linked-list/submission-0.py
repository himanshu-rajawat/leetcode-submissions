# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the length of the list
        curr = head
        n = 0
        while curr:
            n+=1
            curr=curr.next
        #find the mid of the list
        mid = (n+1)//2

        print(mid)
        #1 to mid will be in 1st list and mid+1 to last will be in second which needs to be reversed
        n=1
        curr = head
        while n<mid:
            curr=curr.next
            n+=1
        head2 = curr.next
        curr.next = None

        curr = head2
        prev = None
        #reverse list with head2
        while curr:
           temp = curr.next
           curr.next = prev
           prev = curr
           curr = temp
        head2 = prev

        curr = head
        while head2:
            temp = curr.next
            curr.next = head2
            temp2 = head2.next
            head2.next = temp
            head2 = temp2
            curr = temp


        