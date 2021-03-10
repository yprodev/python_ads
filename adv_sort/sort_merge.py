# Sorts a Python list in ascending order using the merge sort algorithm
def pythonMergeSort(theList):
	# Check the base case - the list contains a single item
	if len(theList) <= 1:
		return theList
	else:
		# Compute the midpoint
		mid = len(theList) // 2

		# Split the list and perform the recursive step
		leftHalf = pythonMergeSort(theList[ :mid])
		rightHalf = pythonMergeSort(thelist[mid: ])

		# Merge the two ordered sublists
		newList = mergeOrderedLists(leftHalf, rightHalf)

		return newList






