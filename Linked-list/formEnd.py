#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    #code here
    temp = head
    table = {}
    c = 1
    
    while temp!=None:
        table[c] = temp.data
        temp = temp.next
        c += 1
    if c-n<1:
        return -1
    else:
        return table[c-n]
