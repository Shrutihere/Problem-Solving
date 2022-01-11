class Solution:
    def isPalindrome(self, head):
        #code here
        temp = head
        s = ""
        
        while temp != None:
            s += str(temp.data)
            temp = temp.next
            
        if s == s[::-1]:
            return 1
        else:
            return 0
