# Implementation of the binary search
def binarySearch(theValues, target):
	# Start with the entire sequence of elements
	low = 0
	high = len(theValues) - 1

	# Repeatedly subdivide the sequende in half until the target is found
	while low <= high:
		# Find the midpoint of the sequence
		mid = (high + low) // 2
		# Does the midpoint contain the target?
		if theValues[mid] == target:
			return True
		# Or does the target precede the midpoint?
		elif target < theValues[mid]:
			high = mid - 1
		else:
			low = mid + 1

	# If the sequence cannot be subdivided further, we're done
	return False

