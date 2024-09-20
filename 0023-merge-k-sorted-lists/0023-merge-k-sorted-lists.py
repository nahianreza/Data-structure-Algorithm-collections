# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        def sortList(l1, l2):
            dummyNode = ListNode()
            tail = dummyNode
            list1 = l1
            list2 = l2
            
            while list1 and list2:
            
                if list1.val > list2.val:
                    tail.next = list2
                    list2 = list2.next
                else:
                    tail.next = list1
                    list1 = list1.next
                tail = tail.next
        
            if list1:
                tail.next = list1
            elif list2:
                tail.next = list2
        
            return dummyNode.next
        
        while len(lists) > 1:
            resList = []
        
            for i in range(0, len(lists), 2):

                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                resList.append(sortList(l1,l2))

            lists = resList

        return lists[0]
        