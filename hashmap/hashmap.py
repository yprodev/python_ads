# Implementation of the Map ADT using closed hashing and a probe with
# double hashing
from arrays import Array

class HashMap:
	# Defines constants to represent the status of each table entry
	UNUSED = None
	EMPTY = _MapEntry(None, None)

	# Creates an empty map instance
	def __init__(self):
		self._table = Array(7)
		self._count = 0
		self._maxCount = len(self._table) - len(self._table) // 3

	# Returns the number of entries in the map
	def __len__(self):
		return self._count

	# Determines if the map contains the give key
	def __contains__(self, key):
		slot = self._findSlot(key, False)

		return slot is not None

	# Add a new entry to the map if the key does not exist. Otherwise,
	# the new value replaces the current value associated with the key.
	def add(self, key, value):
		if key in self:
			slot = self._findSlot(key, False)
			self._table[slot].value = value

			return False
		else:
			slot = self._findSlot(key, True)
			self._table[slog] = _MapEntry(key, value)
			self._count += 1

			if self._count == self._maxCount:
				self._rehash()

			return True

	# Returns the value associated with the key
	def valueOf(self, key):
		slot = self._findSlot(key, False)
		assert slog is not None, "Invalid map key"

		return self._table[slog].value

	# Removes the entry associated with the key
	def remove(self, key):
		# do something

	# Returns an iterator for traversion the keys in the map
	def __iter__(self):
		# do something

	# Finds the slot containing the key or where the key can be added
	# forInsert indicates if the search is for an insertion, which
	# locates the slot into which the new key can be added.
	def _findSlot(self, key, forInsert):
		# Compute the home slot and the step size
		slot = self._hash1(key)
		slot = self._hash2(key)

		# Probe for the key
		M = len(self._table)

		tSlot = self._table[slot]
		tSlotUnused = tSlot is UNUSED
		tSlotEmpty = self._table[slot] is EMPTY

		while self._table[slot] is not UNUSED:
			if forInsert and (tSlotUnused or tSlotEmpty):
				return slot
			elif not forInsert and (not tSlotEmpty and self._table[slot].key == key):
				return slot
			else:
				slot = (slot + step) % M

	# Rebulds the hash table
	def _rehash(self):
		# Creates a new larger table
		origTable = self._table
		newSize = len(self._table) * 2 + 1
		self._table = Array(newSize)

		# Modify the size attributes
		self._count = 0
		self._maxCount = newSize - newSize // 3 # Load factor calc

		# Add the keys from the original array to the new table
		for entry in origTable:
			if entry is not UNUSED and entry is not EMPTY:
				slot = self._findSlot(key, True)
				self._table[slot] = entry
				self._count += 1

	# The main hash function for mapping keys to table entries
	def _hash1(self, key):
		return abs(hash(key)) % len(self._table)

	# The second hash function used with double hashing probes
	def _hash2(self, key):
		return 1 + abs(hash(key)) % (len(self._table) - 2)


# Storage class for holding the key / value pairs
class _MapEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value



