# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy_node = ListNode()
        curr = dummy_node
        prev = None
        while True:
            node = None
            index = None
            for head in lists:
                if head and (not node or node.val>head.val):
                    node = head
                    index = lists.index(head)
            if not node:
                break
            prev = curr
            curr.next = node
            curr = node
            lists[index] = node.next if node.next else None
        
        return dummy_node.next