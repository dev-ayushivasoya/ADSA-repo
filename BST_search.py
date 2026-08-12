class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insert(root,data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left,data)
    else:
        root.right = insert(root.right,data)
    return root

def search(root,key):
    if root is None:
        return False
    if root.data==key:
        return True
    if key<root.data:
        return search(root.left,key)
    else:
        return search(root.right,key)

n=int(input("Enter the number of elements : "))
root=None
for i in range(n):
    data=int(input("Enter element : "))
    root=insert(root,data)
key=int(input("Enter the element to be searched : "))
if search(root,key):
    print("Element found")
else:
    print("Element not found")
