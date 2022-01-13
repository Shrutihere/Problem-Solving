class Solution:

	def matchPairs(self,nuts, bolts, n):
		# code here
		check = { '!':1, '#':2, '$':3, '%':4, '&':5, '*':6, '@':7, '^':8, '~':9}
		hmap = {}
		for i in nuts:
		    if i not in hmap:
		        hmap[i] = check[i]
		newmap = sorted(hmap.items(), key =lambda kv:(kv[1], kv[0]))
		
        for i in range(len(newmap)):
            nuts[i], bolts[i] = newmap[i][0], newmap[i][0]
