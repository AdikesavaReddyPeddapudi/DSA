class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

        # insert

    def insert(self,root,data):
        if root is None:
            return Node(data)        
        if data < root.data:
            root.left = self.insert(root.left,data)
        else:
             root.right = self.insert(root.right,data)
        return root    
        
    def search(self,root,key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)
            
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)

    def find_min(self,root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def delete(self,root,key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left,key)
            
        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            #case 1 : No child
            if root.left is None and root.right is None:
                return None
            # case 2 : One child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # Case 3: Two children
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

bst=BST()
values = [10,3,34,2,7,20]

for v in values:
    bst.root = bst.insert(bst.root,v)

print("Inorder Traversal (Sorted):")
bst.inorder(bst.root)


print("\nInorder before deletion:")
bst.inorder(bst.root)

bst.root = bst.delete(bst.root, 10)

print("\nInorder after deletion:")
bst.inorder(bst.root)