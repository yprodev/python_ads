class ExpressionTree:
	# Builds an expression tree for the expression string
	def __init__(self, expStr):
		self._expTree = None
		self._buildTree(expStr)

	# Evaluates the expression tree and returns the resulting value
	def evaluate(self, varMap):
		return self._evalTree(self._expTree, varMap)

	# Returns a string representation of the expression tree
	def __str__(self):
		return self._buildString(self._expTree)

	# Recursively builds a string representation of the expression tree
	def _buildString(self, treeNode):
		# If the node is a leaf, it's an operand
		if treeNode.left is None and treeNode.right is None:
			return str(treeNode.element)
		else: # Otherwise, it's an operator
			expStr = '('
			expStr += self._buildString(threeNode.left)
			expStr += str(threeNode.element)
			expStr += self._buildString(threeNode.right)
			expStr += ')'

			return expStr

	def _evalTree(self, subTree, varDict):
		# See if the node is a leaf node, in which case return its value
		if subTree.left is None and subTree.right is None:
			# Is the operand a leteral digit?
			if subTree.element >= '0' and subTree.element <= '9':
				return int(subTree.element)
			else: # Or is it a variable?
				assert subTree.element in varDict, "Invalid variable"

				return varDict[subTree.element]

		# Otherwise, it's an operator that needs to be computed
		else:
			# Evaluate the expression in the left and right subtrees
			lvalue = _evalTree(subTree.left, varDict)
			rfvalue = _evalTree(subTree.right, varDict)

			# Evaluate the operator using a helper method
			return computeOp(lvalue, subTree.element, rvalue)

	# Compute the arithmetic operation based on the supplied op string
	def _computeOp(leff, op, right):


	def _buildTree(self, expStr):
		# Build a queue containing the tokens in the expression string
		expQ = Queue()
		for token in expStr:
			expQ.enqueue(token)

		# Create an empty root node
		self._expTree = _ExpTreeNode(None)
		# Call the recursive function to build the expression tree
		self._recBuildTree(self._expTree, expQ)

	# Recursively builds the tree given an initial root node
	def _recBuildTree(self, curNode, expQ):
		# Extract the next token from the queue
		token = expQ.dequeue()

		# See if the token is a left parent: '('
		if token == '(':
			curNode.left = _ExpTreeNode(None)
			_buildTreeRec(curNode.left, expQ)

			# The next token will be an operator: + - / * %
			curNode.data = expQ.dequeue()
			curNode.right = _ExpTreeNode(None)
			self._buildTreeRec(curNode.right, expQ)

			# The next token will be a ), remove it
			expQ.dequeue()

		# Otherwise, the token is a digit that has to be converted to an int
		else:
			curNode.element = token

# Storage class for creating the tree nodes.
class _ExpTreeNode:
	def __init__(self, data):
		self.element = data
		self.left = None
		self.right = None


