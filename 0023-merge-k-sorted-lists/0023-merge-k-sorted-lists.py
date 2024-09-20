# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode()
        dummyTail = dummy
        
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
        
        if lists[0]:
            dummyTail.next = lists[0]
        
        for i in range(1,len(lists)):
            dummyTail.next = sortList(dummy.next,lists[i])
            
            
        return dummy.next
                
        