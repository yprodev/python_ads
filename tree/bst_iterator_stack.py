class _BSTMapIterator:
	def __init__(self, root):
		# Create a stack for use in traversing the tree
		self._theStack = Stack()
		# We must traverse down to the node containing the smalles key
		# during which each node along the path is pushed onto the stack
		self._traverseToMinNode(root)

	def __iter__(self):
		return self

	# Returns the next item from the BST in key order
	def __next__(self):
		# If the stack is empty, we are done
		if self._theStack.isEmpty():
			raise StopIteration
		else:
			# The top node on the stack contains the next key
			node = self._theStack.pop()
			key = node.key
			# If this node has a subtree rooted as the right child, we must
			# find the node in that subtree that contains the smalles key.
			# Again, the nodes along the path are pushed onto the stack.
			if node.right is not None:
				self._traverseToMinNode(node.right)

	# Traverse down the subtree to find the node containing the smallest
	# key during which the nodes along that path are pushed onto the stack
	def _traverseToMinNode(self, subtree):
		if subtree is not None:
			self._theStack.push(subtree)
			self._traverseToMinNode(subtree.left)


