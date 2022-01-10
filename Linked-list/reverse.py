    def reverseList(self, head):
        # Code here
        if head == None or head.next == None:
            return head
        if head.next.next == None:
            temp = head.next
            x = head.data
            head.data = temp.data
            temp.data = x
            return head
        prev = None
        temp = head
        nextt = temp.next
        while temp.next != None:
            temp.next = prev
            prev = temp
            temp = nextt
            if nextt != None:
                nextt = nextt.next
        temp.next = prev
        head = temp
        return head
