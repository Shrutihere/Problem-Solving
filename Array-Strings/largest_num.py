class Solution:

	def printLargest(self,arr):
	    # code here
	   # str_arr = [str(i)*10 for i in arr]
	   # str_arr.sort(reverse=True)
	   # print(str_arr)
	   A = sorted(arr,key=lambda x:str(x)*10,reverse=True)
       ans = ''.join([str(i)for i in A])
       return ans
