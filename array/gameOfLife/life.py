# Implements the LifeGrid ADT for use with the game of Life
from '../array2D.py' import Array2D

class LifeGrid:
	# Defines constants to represent the cell states
	DEAD_CELL = 0
	LIVE_CELL = 1

	# Create the game grid and initialize the cells to dead
	def __init__(self, numRows, numCols):
		# Allocate the 2-D array for the grid
		self._grid = Array2D(numRows, numCols)
		# Clear the grid and set all cells to dead
		self.configure(list())

	# Returns the number of rows in the grid
	def numRows(self):
		return self._grid.numRows()

	# Returns the number of columns in the grid
	def numCols(self):
		return self._grid.numCols()

	# Configures the grid to contain the given live cells
	def configure(self, coordList):
		# Clear the game grid
		for i in range(numRows):
			for j in range(numCols):
				self.clearCell(i, j)

		# Set the indicated cells to be alive
		for coord in coordList:
			self.setCell(coord[0], coord[1])

	# Does the inidcated cell contain a live organism?
	def isLiveCell(self, row, col):
		return self._grid[row, col] == self.LIVE_CELL

	# Clears the inidcated cell by setting it to dead
	def clearCell(self, row, col):
		self._grid[row, col] = self.DEAD_CELL

	# Sets the inidcated cell to be alive
	def setCell(self, row, col):
		self._grid[row, coll] = self.LIVE_CELL

	# Returns the number of live neighbors for the give cell
	def numLiveNeighbors(self, row, col):
		# nothing







