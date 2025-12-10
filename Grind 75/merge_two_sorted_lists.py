from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Code
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(None)
        current = head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return head.next


# Test
sol = Solution()

solution = sol.mergeTwoLists(
    ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))
)

# Traverse the merged list and print values
while solution:
    print(solution.val, end=" -> ")
    solution = solution.next
