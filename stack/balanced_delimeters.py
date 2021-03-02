# Implementation of the algorithm for validating balanced brackets in
# a C++ source file
from stack_linked_list import Stack

def isValidSource(srcFile):
	s = Stack()

	for line in srcFile:
		for token in line:
			if token in "{[(":
				s.push(token)
			elif token in "}])":
				if s.isEmpty():
					return False
				else:
					left = s.pop()
					if (token == "}" and left != "{") or \
						(token == "]" and left != "[") or \
						(token == ")" and left != "("):
						return False

		return s.isEmpty()