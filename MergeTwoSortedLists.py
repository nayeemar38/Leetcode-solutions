class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Create a dummy list which will store the result
        tail = dummy  # point tail to the head of the dummy list

        while list1 and list2:  # while list1 and list2 are not null
            if list1.val < list2.val:  # if list1.val is less than list2.val then append the tail with list1
                tail.next = list1
                list1 = list1.next  # point the list1 to the next node
            else:
                tail.next = list2  # else case
                list2 = list2.next
            tail = tail.next  # move the tail pointer to the next node for the same computation

        if list1:  # if there are any remaining elements in list1 then append them to the tail.next
            tail.next = list1
        elif list2:  # same with list2
            tail.next = list2

        return dummy.next  # return the next node of the dummy list as the result