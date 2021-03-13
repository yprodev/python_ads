def inorderTrav(subTree):
	if subTree is not None:
		inorderTrav(subTree.left)
		print(subTree.data)
		inorderTrav(subTree.right)

