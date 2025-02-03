class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"({self.key}: {self.value})"
    
def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)
    
def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)
    
def insert_bst(root, node):
    if root == None:
        return node
    
    if node.key == root.key:
        return root
    
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)
    return root

def delete_bst(root, key):
    if root == None:
        return root
    
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    else:
        if root. left == None:
            return root.right
        
        if root.right == None:
            return root.right
        
        succ = root.right 
        while succ.left != None:
            succ = succ.left

        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)
    
    return root

def preorder(n):
    if n is not None:
        print('{', end=' ')
        print(n, end=' ')
        preorder(n.left)
        preorder(n.right)
        print('}', end = ' ')