from maximum_subarray_sum.functions01 import maximum_subarray_sum
from maximum_subarray_sum.functions02 import maxSubarraySum

arr = [5, 4, 1, 7, 8] 
arr01 = [16, 8, -8, -2, -1]
arr02 = [2, 3, -8, 7, -1, 2, 3]
arr03 = [-2, -4]

def main01():
	print(maximum_subarray_sum(arr01))

def main02():
	print(maxSubarraySum(arr02))