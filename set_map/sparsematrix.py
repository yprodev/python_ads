# Implementation of the Sparse Matrix ADT using a list

class SparseMatrix:
	# Creates a sparese matrix of size numRows x numCols initialized to 0.
	def __init__(self, numRows, numCols):
		self._numRows = numRows
		self._numCols = numCols
		self._elementList = list()

	# Return the number of rows in the matrix
	def numRows(self):
		return self._numRows

	# Return the number of cols in the matrix
	def numCols(self):
		return self._numCols

	# Return the value of element (i, j): x[i, j]
	def __getitem__(self, ndxTuple):
		# ...implement yourself

	# Set the value of element (i, j) to the value s: x[i, j] = s
	def __setitem__(self, ndxTuple, scalar):
		ndx = self._findPosition(ndxTuple[0], ndxtuple[1])
		if ndx is not None: # if the element is found in the list
			if scalar != 0.0:
				self._elementList[ndx].value = scalar
			else:
				self._elementList.pop(ndx)
		else:
			if scalar != 0.0:
				element = _MatrixElement(ndxTuple[0], ndxTuple[1], scalar)
				self._elementList.append(element)

	# Scale the matrix by the given scalar
	def scaleBy(self, scalar):
		for element in self._elementList:
			element.value *= scalar

	# The additional methods should be placed here...
	def __add__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self.numRows() and \
			rhsMatrix.numCols() == self.numCols(), \
			"Matrix size not compatible for the add operation."

		# Create the new matrix
		newMatrix = SparseMatrix(self.numRows(), self.numCols())

		# Duplicate the lhs matrix. The elements are mutable, thus we must
		# create new objects and not simply copy the references.
		for element in self._elementList:
			dupElement = _MatrixElement(element.row, element.col, element.value)
			newMatrix._elementList.append(dupElement)

		# Iterate through each non-zero element of the rhsMatrix
		for element in rhsMatrix._elementList:
			# Get the value of the corresponding element in the new matrix
			value = newMatrix[element.row, element.col]
			value += element.value
			# Store the new value back to the new matrix
			newMatrix[element.row, element.col] = value

		return newMatrix


	# def __sub__(self, rhsMatrix):
	# def __mul__(self, rhsMatrix):

	# Helper method used to find a specific matrix element (row, col) in the
	# list of non-zero entries. None is returned if the element is not found.
	def _findPosition(self, row, col):
		n = len(self._elementList)
		for i in range(n):
			if row == self._elementList[i].row and \
				col == self._elementList[i].col:
				return i # Return the index of the element if found
		return None # Return None when the element is zero.

# Storage class for holding the non-zero matrix elements
class _MatrixElement:
	def __init__(self, row, col, value):
		self.row = row
		self.col = col
		self.value = value









