# Constants for the balance factors
LEFT_HIGH = 1
EQUAL_HIGH = 0
RIGHT_HIGH = -1

# Implementation of the Map ADT using an AVL tree
class AVLMap:
	def __init__(self):
		self._root = None
		self._size = 0

	def __len__(self):
		return self._size

	def __contains__(self, key):
		return self._bstSearch(self._root, key) is not None

	def add(self, key, value):
		node = self._bstSearch(key)
		if node is not None:
			node.value = value
			return False
		else:
			(self._root, tmp) = self._avlInsert(self._root, key, value)
			self._size += 1
			return True

	def valueOf(self, key):
		node = self._bstSearch(self._root, key)
		assert node is not None, "Invalid map key"

		return node.value

	def remove(self, key):
		assert key in self, "Invalid map key"
		(self._root, tmp) = self._avlRemove(self._root, key)
		self._size -= 1

	def __iter__(self):
		return _BSTMapIterator(self._root)

# Storage class for creating the AVL tree node
class _AVLMapNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.bfactor = EQUAL_HIGH
		self.left = None
		self.right = None



