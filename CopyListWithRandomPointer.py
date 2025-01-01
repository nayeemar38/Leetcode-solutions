class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # If the head is None, return None immediately (empty list case)
        if not head:
            return None

        # Dictionary to map old nodes to their copied nodes
        old_to_new = {}

        # Step 1: Create a copy of each node and map old nodes to their copies
        curr = head
        while curr:
            # Create a new Node with the same value as the current node
            old_to_new[curr] = Node(curr.val)
            # Move to the next node in the original list
            curr = curr.next

        # Step 2: Set the next and random pointers for the copied nodes
        curr = head
        while curr:
            # Set the next pointer for the copied node using the mapping
            old_to_new[curr].next = old_to_new.get(curr.next)
            # Set the random pointer for the copied node using the mapping
            old_to_new[curr].random = old_to_new.get(curr.random)
            # Move to the next node in the original list
            curr = curr.next

        # Return the copy of the head node, which is the head of the deep-copied list
        return old_to_new[head]
