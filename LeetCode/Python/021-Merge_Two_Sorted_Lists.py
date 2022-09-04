from typing import (Optional,)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def validate(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> None:
        # The number of nodes in both lists is in the range [0, 50]
        assert all([-100 <= el <= 100 for el in list1+list2])
        # Both list1 and list2 are sorted in non-decreasing order.

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2

        seek, target = (list1, list2) if list1.val < list2.val else (
            list2, list1)
        head = seek
        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next
        return head


if __name__ == "__main__":
    s = Solution()

    tests = [
        ([], [], []),
        ([], [0], [0]),
        # ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ]

    for test in tests:
        exec("assert s.mergeTwoLists(test[0], test[1]) == test[2]")

    print("Well done!")
