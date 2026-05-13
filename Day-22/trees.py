from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None
        
    def height(root):


def level_order(root):
    if not root:
        return
    
    q = deque([root])

    while q:
        node = q.popleft()
        print(node.data, end = ' ')

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Total Nodes :",count_nodes(root))
    print("Height : ",height(root))
    print("Leaf Nodes:",count_leaves(root))
    print("Level order :")
    level_order(root)
main()