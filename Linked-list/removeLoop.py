class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        temp = head
        table={}
        table[temp] = 1
        
        while temp!=None:
            if temp.next not in table:
                table[temp.next] = 1
            else:
                temp.next = None
            temp = temp.next
