def preorderTrav(subTree):
	if subTree is not None:
		print(subTree.data)
		preorderTrav(subTree.left)
		preorderTrav(subTree.right)

