#Function to merge two sorted linked list.
def sortedMerge(head1, head2):
    # code here
    temp1 = head1
    temp2 = head2
    if temp1.data<temp2.data:
        head3 = temp1
        temp1 = temp1.next
    else:
        head3 = temp2
        temp2 = temp2.next
    
    temp3 = head3
    
    while temp1!=None and temp2!=None:
        # print(head3.data)
        if temp1.data<temp2.data:
            x = temp1.next
            temp3.next = temp1
            temp3 = temp3.next
            temp1 = x
        else:
            x = temp2.next
            temp3.next = temp2
            temp3 = temp3.next
            temp2 = x
        
    if temp1 == None and temp2!=None:
        temp3.next = temp2
    if temp2 == None and temp1!=None:
        temp3.next = temp1
    return head3
