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

	# Determines if the map contains the given key
	def __contains__(self, key):
		return self._bstSearch(self._root, key) is not None

	# Returns the value associated with the key
	def valueOf(self, key):
		node = self._bstSearch(self._root, key)
		assert node is not None, "Invalid map key"

		return node.value

	# Helper method that recursively searches the tree for a target key
	def _bstSearch(self, subtree, target):
		if subtree is None: # Base case
			return None
		elif target < subtree.key: # target is left of the subtree root
			return self._bstSearch(subtree.left)
		elif target > subtree.key: # target is right of the subtree root
			return self._bstSearch(subtree.right)
		else: # Base case
			return subtree

	# Helper method for finding the node containing the minimum key
	def _bstMinimum(self, subtree):
		if subtree is None:
			return None
		elif subtree.left is None:
			return subtree
		else:
			return self._bstMinimum(subtree.left)


# Storage class for the binary search tree nodes of the map
class _BSTMapNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None


