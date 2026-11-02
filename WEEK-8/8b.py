
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left is None:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    def search(self, key):
        if self.root is None:
            return False

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.data == key:
                return True

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        return False

    def delete(self, key):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [(self.root, None)]
        target = None
        deepest = None
        parent = None

        while queue:
            temp, par = queue.pop(0)
            deepest = temp
            parent = par

            if temp.data == key and target is None:
                target = temp

            if temp.left:
                queue.append((temp.left, temp))

            if temp.right:
                queue.append((temp.right, temp))

        if target is None:
            print("Value not found")
            return

        target.data = deepest.data

        if parent is None:
            self.root = None
        elif parent.right == deepest:
            parent.right = None
        else:
            parent.left = None

        print("Node deleted")

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def display(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)


# Main program
bt = BinaryTree()

while True:
    print("\n\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        bt.insert(value)

    elif choice == 2:
        value = int(input("Enter value to search: "))
        if bt.search(value):
            print("Value found")
        else:
            print("Value not found")

    elif choice == 3:
        value = int(input("Enter value to delete: "))
        bt.delete(value)

    elif choice == 4:
        print("Inorder Traversal:")
        bt.inorder(bt.root)

    elif choice == 5:
        print("Preorder Traversal:")
        bt.preorder(bt.root)

    elif choice == 6:
        print("Postorder Traversal:")
        bt.postorder(bt.root)

    elif choice == 7:
        print("Level Order:")
        bt.display()

    elif choice == 8:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
