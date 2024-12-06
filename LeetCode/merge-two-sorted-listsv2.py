from typing import List
from typing import Optional


# Need to review
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        current1 = list1

        while list1 and list2:
            if list1.next and list1.next.val <= list2.val:
                list1 = list1.next
            else:
                temp = list2.next
                list2.next = list1.next
                list1.next = list2
                list2 = temp
                list1 = list1.next

        if list2:
            list1.next = list2

        return current1



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
