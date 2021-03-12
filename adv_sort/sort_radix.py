# Sorts a sequence of positive integers using the radix sort algorithm

from 'queue/queue_linked_list' import Queue
from 'array/array' import Array

def radisSort(intList, numDigits):
	# Create an array of queues to represent the bins
	NUM_BINS = 10

	binArray = Array(NUM_BINS)
	for k in range(NUM_BINS):
		binArray[k] = Queue()

	# The value of the current column
	column = 1

	# Iterate over the number of digits in the larges value
	for d in range(numDigits):

		# Distribute the keys accross the 10 bins
		for key in intList:
			digit = (key // column) % NUM_BINS
			binArray[digit].enqueue(key)

		# Gather the keys from the bins and place them back in intList
		i = 0
		for bin in binArray:
			while not bin.isEmpty():
				intList[i] = bin.dequeue()
				i += 1

		# Advance to the next column value
		column *= NUM_BINS


