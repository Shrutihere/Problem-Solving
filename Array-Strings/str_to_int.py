class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        # Code here
        # try:
        #     return int(string)
        # except:
        #     return -1
        hmap = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,}
        ans=0
        neg=False
        for i in string:
            if i =='-':
                neg=True
                continue
            if i not in hmap:
                return -1
            else:
                ans = (ans*10)+hmap[i]
        if neg:
            return -ans
        else:
            return ans
