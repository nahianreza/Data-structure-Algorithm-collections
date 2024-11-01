# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    tail.next = l2
                    l2 = l2.next
                else:
                    tail.next = l1
                    l1 = l1.next
                tail = tail.next
            
            if l2:
                tail.next = l2
            else:
                tail.next = l1
            return dummy.next
        

        def dfs(root):
            if not root.next:
                return root

            slow, fast = root, root.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next


            list1 = root
            temp = slow.next
            slow.next = None
            list2 = temp

            list1 = dfs(list1)
            list2 = dfs(list2)
            return merge(list1, list2)

        return dfs(head)



        