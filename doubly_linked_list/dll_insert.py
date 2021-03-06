# Given a head and tail reference and a new value, add the new value
# to a sorted doubly linked list
newNode = DListNode(value)

if head is None: # empty list
	head = newNode
	tail = head
elif value < head.data: # insert before head
	newNode.next = head
	head.prev = newNode
	head = newNode
elif value > tail.data: # insert after tail
	newNode.prev = tail
	tail.next = newNode
	tail = newNode
else: # inser in the middle
	node = head
	while node is not None and node.data < value:
		node = node.next

	newNode.next = node
	newNode.prev = node.prev
	node.prev.next = newNode
	node.prev = newNode

