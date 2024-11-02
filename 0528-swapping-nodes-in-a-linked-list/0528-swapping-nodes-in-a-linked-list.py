# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = []

        dummy = ListNode()
        tail = dummy

        cur = head

        while cur:
            res.append(cur.val)
            cur = cur.next
         
        res[k -1], res[len(res) - k] = res[len(res) - k], res[k -1]

        print(res)

        for i in res:
            tail.next = ListNode(i)
            tail = tail.next
        
        return dummy.next
        