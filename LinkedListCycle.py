class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use a hash set for a lookup to verify looping
        visited_nodes = set()
        current = head

        while current:
            if current in visited_nodes:
                return True
            visited_nodes.add(current)
            current = current.next

        return False