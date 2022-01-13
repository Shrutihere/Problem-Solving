class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        hmap = {}
        for i in s:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1
        for i in s:
            if hmap[i]==1:
                return i
        return '$'
