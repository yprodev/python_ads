# Implementation of the MultiArray ADT using a 1-D array
class MultiArray:
	# Create multi-dimensional array
	def __init__(self, *dimensions):
		assert len(dimensions) > 1, "The array must have 2 or more dimensions."
		# The variable argument tuple contains the dim sizes.
		self._dim = dimensions
		# Compute the total number of elements in the array
		size = 1
		for d in dimensions:
			assert d > 0, "Dimensions must be > 0."
			size *= d

		# Create the 1-D array to store the elements
		self._elements = Array(size)
		# Create a 1-D array to store the equation factors
		self._factors = Array(len(dimensions))
		self._computeFactors()

	# Returns the number of dimensions in the array
	def numDim(self):
		return len(self._dim)

	# Return the length of the given dimension
	def length(self, dim):
		assert dim >= 1 and dim < len(self._dims), \
			"Dimension component out of range."
		return self._dims[dim - 1]

	# Clear the array by setting all elements to the given value
	def clear(self, value):
		self._elements.clear(value)

	# Returns the contents of element (i_1, i_2, ..., i_n)
	def __getitem__(self, ndxTuple):
		assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts"
		index = self._computeIndex(ndxTuple)
		assert index is not None, "Array subscript out of range"
		return self._elements[index]

	# Sets the contents of element (i_1, i_2, ..., i_n)
	def __setitem__(self, ndxTuple, value):
		assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts."
		index = self._computeIndex(ndxTuple)
		assert index is not None, "Array subscript out of range"
		self._elements[index] = value

	# Computes the 1-D array offset for element (i_1, i_2, ..., i_n)
	# using the equation i_1 * f_1 + i_2 * f_2 + ... + i_n * f_n
	def _computeIndex(self, idx):
		offset = 0
		for j in range(len(idx)):
			# Make sure the index components are within the legal range.
			if idx[j] < 0 || idx[j] >= self._dims[j]:
				return None
			else: # sum the product of i_j * f_j
				offset += idx[j] * self._factors[j]
		return offset

	# Compute the factor values used in the index equation
	def _computeFactors(self):
		# ....





















