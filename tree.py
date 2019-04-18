#components in tree
class Node:
	def __init__(self, key, value, left=None, right=None):
		self.key = key
		self.value = value
		self.right = right
		self.left = left

#functions in the tree
class Tree:
	def __init__(self):
		self.root = None

	def contains(self, key):
		found = False
		current = self.root
		while current != None and found == False:
			if current.key == key:
				found = True
			elif key < current.key:
				current = current.left
			else:
				current = current.right

		return found

	# for adding the nodes in the tree using the concept of the binary tree 
	#,i.e, left nodes are smaller than the root node and the right node is larger than the root node
	def add(self, key, value):
		if self.root == None:
			self.root = Node(key, value)
		else:
			current = self.root
			while current != None:
				if current.key == key:
					current.value = value
					break
				elif key < current.key:
					if current.left == None:
						current.left = Node(key, value)
						break
					current = current.left
				else:
					if current.right == None:
						current.right = Node(key, value)
						break
					current = current.right
				
	
	#It gives the value of the key 
	def get(self, key):
		current = self.root
		while current != None:
			if current.key == key:
				return current.value
			elif key < current.key:
				current = current.left
			else:
				current = current.right

		return None
	#Here we are using recursion with backtracking if the node doesn't has child nodes

	def traverse(self, current, arr):
		if current != None:
			arr.append(current.key)
			self.traverse(current.left, arr)
			self.traverse(current.right, arr)


	def keys(self):
		arr = []
		self.traverse(self.root, arr)
		return arr

	def values(self):
		ks = self.keys()
		return [self.get(k) for k in ks]

#Insertions in the tree 
tree = Tree()
tree.add("a", 2)
tree.add("c", 4)
tree.add("b", 5)
tree.add("d", 4)
print(tree.keys())
print(tree.values())
print(tree.get("c"))
print(tree.contains("a"))