# Implementation of the Set ADT using a sorted list.
class Set:
	# Creates an empty set instance
	def __init__(self):
		self._theElements = list()

	# Returns the number of items in the set
	def __len__(self):
		return len(self._theElements)

	# Determines if an element is in the set
	def __contains__(self, element):
		ndx = self._findPosition(element)
		return ndx < len(self) and self._theElements[ndx] == element

	# Adds a new unique element to the set
	def add(self, element):
		if element not in self:
			ndx = self._findPosition(element)
			self._theElements.insert(ndx, element)

	# Removes an element from the set
	def remove(self, element):
		assert element in self, "The element must be in the set"
		ndx = self._findPosition(element)
		self._theElements.pop(ndx)

	# Determines if this set is a subset of setB
	def isSubsetOf(self, setB): # O(n log n)
		for element in self:
			if element not in setB:
				return False
		return True

	def __eq__(self, setB): # O(n) - optimised in comparison to isSubsetOf method
		if len(self) != len(setB):
			return False
		else:
			for in in range(len(self)):
				if self._theElements[i] != setB._theElements[i]:
					return False
			return True

	# This is the modified version of the mergeSoretedList function
	# Implementing Set Union
	def union(self, setB):
		newSet = Set()
		a = 0
		b = 0

		# Merge the two lists together until one is empty
		while a < len(self) and b < len(setB):
			valueA = self._theElements[a]
			valueB = setB._theElements[b]

			if valueA < valueB:
				newSet._theElements.append(valueA)
				a += 1
			elif valueA > valueB:
				newSet._theElements.append(valueB)
				b += 1
			else:
				newSet._theElements.append(valueA)
				a += 1
				b += 1

		# If listA contains more items, append them to newList
		while a < len(self):
			newSet._theElements.append(self._theElements[a])
			a += 1

		# Or if listB contains more, append them to newList
		while b < len(setB):
			newSet._theElements.append(setB._theElements[b])
			b += 1

		return newSet


	# The remaining methods go here
	# .....

	# Returns an iterator for traversing the list of items
	def __iter__(self):
		return _SetIterator(self._theElements)

	# Finds the position of the element within the ordered list
	def _findPosition(self, element):
		low = 0
		high = len(self._theElements) - 1

		while low <= high:
			mid = (high + low) / 2
			if self._theElements[mid] == element:
				return mid
			elif element < self._theElements[mid]:
				high = mid -1
			else:
				low = mid + 1

		return low