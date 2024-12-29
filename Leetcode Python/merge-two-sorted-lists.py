from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummy.next

def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head

if __name__ == "__main__":
    solution = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]
    result = solution.mergeTwoLists(createLinkedList(list1), createLinkedList(list2))
    print(result)
