import ctypes

ArrayType = ctypes.py_object * 5
slots = ArrayType()

for i in range(5):
	slots[i] = None


# Adding elements to the array
slots[1] = 12
slots[3] = 54
slots[4] = 37

# Removing the element from the array
slots[3] = None

print(slots[0])