class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        carry=0

        while l1 or l2 or carry:  # Handle cases with lists of different lengths
            digit1 = l1.val if l1 else 0  # Handle potential null pointers
            digit2 = l2.val if l2 else 0
            sum = digit1 + digit2 + carry

            digit = sum % 10
            carry = sum // 10  # Integer division for handling carry

            current.next = ListNode(digit)
            current = current.next

            l1 = l1.next if l1 else None  # Avoid unnecessary operations if l1 is null
            l2 = l2.next if l2 else None

        return dummyHead.next  # Return the actual list (skip dummy node)