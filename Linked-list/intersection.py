#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    #code here
    temp1 = head1
    temp2 = head2
    table = {}
    
    while temp1 != None or temp2 != None:
        if temp1 not in table and temp1!=None:
            table[temp1] = 1
        elif temp1!=None:
            return temp1.data
            
        if temp2 not in table and temp2!=None:
            table[temp2] = 1
        elif temp2!=None:
            return temp2.data
            
        if temp1!=None:
            temp1 = temp1.next
        if temp2!=None:
            temp2 = temp2.next
