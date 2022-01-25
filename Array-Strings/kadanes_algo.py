class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        curr = 0
        j = 0
        maxx = -99999
        
        for i in range(len(arr)):
            curr += arr[i]
            if arr[i] > curr:
                j = i
                curr = arr[i]
            if curr>maxx:
                maxx = curr
        return maxx
