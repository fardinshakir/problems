from typing import List
from typing import Optional


# Need to review
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next

            cur = cur.next

        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]
    result = solution.mergeTwoLists(list1, list2)
    print(result)
