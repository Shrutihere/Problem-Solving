class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        temp = head
        obj = {}
        while temp != None:
            if temp not in obj:
                obj[temp] = 1
            else:
                return True
            temp = temp.next
            # print(obj)
        return False
