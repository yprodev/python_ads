def postorderTrav(subTree):
	if subTree is not None:
		postorderTrav(subTree.left)
		postorderTrav(subTree.right)
		print(subTree.data)

