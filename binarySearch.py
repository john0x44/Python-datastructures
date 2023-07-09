#Description : binary search implementation 
#time complexity : O(log n)


def search(nums,target):
	l,r = 0,len(nums)-1 

	while l<=r:
		m = l + ((r-l)//2)

		if nums[m] > target:
			r = m - 1 
		elif nums[m] < target:
			l = m + 1 
		else:
			return m 
	return -1 

nums = [1,2,3,4,5,6,7]
print(search(nums,3))