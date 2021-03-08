# Performs a recursive binary search on a sorted sequence
def recBinarySearch(target, theSeq, first, last):
	# If the sequence cannot be subdivided further, we are done
	if first > last:
		return False # Base case 1
	else:
		# Find the midpoint of the sequence
		mid = (last + first) // 2
		# Does the alement at the midpoint contain the target?
		if theSeq[mid] == target:
			return True # Base case 2
		# Or does the target preced the element at the midpoint?
		elif target < theSeq[mid]:
			return recBinarySearch(target, theSeq, first, mid - 1)
		# Or does it follows the element at the midpoint?
		else:
			return recBinarySearch(target, theSeq, mid + 1, last)

