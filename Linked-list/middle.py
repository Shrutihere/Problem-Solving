class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        slow, fast = head, head
        
        while fast!=None:
            if fast.next == None:
                return slow.data
            if fast.next.next == None:
                return slow.next.data
            slow = slow.next
            fast = fast.next.next
