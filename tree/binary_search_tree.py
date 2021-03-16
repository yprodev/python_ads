class BSTMap:
	# Creates an empty map instance
	def __init__(self):
		self._root = None
		self._size = 0

	# Returns the number of entries in the map
	def __len__(self):
		return self._size

	# Returns an iterator for traversing the keys in the map
	def __iter__(self):
		return _BSTMapIterator(self._root)

# Storage class for the binary search tree nodes of the map
class _BSTMapNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None


