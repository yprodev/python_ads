# Implementation of the Set ADT container using a Python list.
class Set:
	# Create an empty set instance
	def __init__(self):
		self._theElements = list()

	# Return the number of items in the set
	def __len__(self):
		return len(self.__theElements)

	# Determines if an element is in the set
	def __contains__(self, element):
		return element in self._theElements

	# Add a new unique element to the set
	def add(self, element):
		if element not in self: # ??? self._theElements
			self._theElements.append(element)

	# Remove an element from the set
	def remove(self, element):
		assert element in self, "The element must be in the set"
		self._theElements.remove(item)

	# Determine if two sets are equal
	def __eq__(self, setB):f
		if len(self) != len(setB):
			return False
		else:
			return self.isSubsetOf(setB)

	# Determine if this set is a subset of setB
	def isSubsetOf(self, setB):
		for element in self: # ??? self._theElements
			if element not in setB:
				return False
		return True

	# Create a new set from the union of this set and setB
	def union(self, setB):
		newSet = Set()
		newSet._theElements.extend(self._theElements)
		for element in setB:
			if element not in self:
				newSet._theElements.append(element)

		return newSet

	# Create a new set from the intersection: self set and setB
	def interset(self, setB):
		# nothing

	# Create a new set from the difference: self set and setB
	def difference(self, setB):
		# nothing

	# Return an iterator for traversing the list of items
	def __iter__(self):
		return _SetIterator(self._theElements)



