class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        # Create a dummy node that points to the head of the list.

        dummy = ListNode(0, head)

        # Initialize prev as the dummy node.

        prev = dummy

        # Move 'prev' to the node just before the `left` position (1-based index).
        for _ in range(left - 1):
            prev = prev.next


        current = prev.next

        # Reverse the sublist between `left` and `right`.

        for _ in range(right - left):
            # Temporarily store the node after `current` in 'next_node'.
            next_node = current.next

            # Perform the swap operations:

            current.next, next_node.next, prev.next = next_node.next, prev.next, next_node

        # Return the new head of the list, which is the next node of the dummy (in case the head has changed).
        return dummy.next