from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
    
def make_list(values):
    dummy = ListNode()
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next


l1 = make_list([2, 4, 3])
l2 = make_list([5, 6, 4])

solution = Solution()
answer = solution.addTwoNumbers(l1, l2)

print_list(answer)