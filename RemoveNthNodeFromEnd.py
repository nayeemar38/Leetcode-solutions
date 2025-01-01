class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize a dummy node to simplify the removal logic
        dummy = ListNode(0, head)
        # Initialize two pointers, both starting from the dummy node
        first, second = dummy, dummy

        # Move the first pointer `n + 1` steps ahead to create a gap of `n` nodes between first and second
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until the first pointer reaches the end of the list
        while first is not None:
            first = first.next
            second = second.next

        # At this point, second pointer is just before the node to be removed
        # Remove the nth node from the end by adjusting the pointers
        second.next = second.next.next

        # Return the head of the modified list, skipping the dummy node
        return dummy.next