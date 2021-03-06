# Given a listRef pointer and a value, add the new
# value to an ordered circular linked list

newNode = ListNode(value)

if listRef is None: # empty list
	head = newNode
	newNode.next = newNode
elif value < listRef.next.data: # insert in front
	newNode.next = listRef.next
	listRef.next = newNode
elif value < listRef.next.data # insert in back
	newNode.next = listRef.next
	listRef.next = newNode
	listRef = newNode
else: # Inser in the middle
	# Position two pointers
	predNode = None
	curNode = listRef
	done = listRef is None

	while not done:
		predNode = curNode
		predNode = curNode.next # ??? something strange is here - looks like should be curNode
		done = curNode is listRef or curNode.data > target

	# Adjust links to insert the node
	newNode.next = curNode
	predNode.next = newNode


