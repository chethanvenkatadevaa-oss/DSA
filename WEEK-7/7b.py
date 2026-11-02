
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Create Binary Tree
    def create(self):
        data = int(input("Enter root node: "))
        self.root = Node(data)
        print("Binary Tree created successfully")

    # Insert Operation
    def insert(self):
        data = int(input("Enter element to insert: "))
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            print("Node inserted successfully")
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left is None:
                temp.left = new_node
                print("Node inserted successfully")
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                print("Node inserted successfully")
                return
            else:
                queue.append(temp.right)

    # Search Operation
    def search(self):
        data = int(input("Enter element to search: "))

        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.data == data:
                print("Element found")
                return

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        print("Element not found")

    # Delete Operation
    def delete(self):
        data = int(input("Enter element to delete: "))

        if self.root is None:
            print("Tree is empty")
            return

        queue = [(self.root, None)]
        target = None
        last = None
        parent = None

        while queue:
            temp, par = queue.pop(0)
            last = temp
            parent = par

            if temp.data == data and target is None:
                target = temp

            if temp.left:
                queue.append((temp.left, temp))

            if temp.right:
                queue.append((temp.right, temp))

        if target is None:
            print("Element not found")
            return

        if last == target:
            if parent is None:
                self.root = None
            elif parent.left == last:
                parent.left = None
            else:
                parent.right = None
        else:
            target.data = last.data

            if parent.left == last:
                parent.left = None
            else:
                parent.right = None

        print("Node deleted successfully")

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Display Binary Tree
    def display(self):
        if self.root is None:
            print("Tree is empty")
        else:
            print("Binary Tree elements (Level Order):")
            queue = [self.root]

            while queue:
                temp = queue.pop(0)
                print(temp.data, end=" ")

                if temp.left:
                    queue.append(temp.left)

                if temp.right:
                    queue.append(temp.right)

            print()


# Main Program
bt = BinaryTree()

while True:
    print("\n----- BINARY TREE USING LINKED LIST -----")
    print("1. Create Binary Tree")
    print("2. Insert")
    print("3. Search")
    print("4. Delete")
    print("5. Inorder Traversal")
    print("6. Preorder Traversal")
    print("7. Postorder Traversal")
    print("8. Display")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bt.create()
    elif choice == 2:
        bt.insert()
    elif choice == 3:
        bt.search()
    elif choice == 4:
        bt.delete()
    elif choice == 5:
        print("Inorder:", end=" ")
        bt.inorder(bt.root)
        print()
    elif choice == 6:
        print("Preorder:", end=" ")
        bt.preorder(bt.root)
        print()
    elif choice == 7:
        print("Postorder:", end=" ")
        bt.postorder(bt.root)
        print()
    elif choice == 8:
        bt.display()
    elif choice == 9:
        print("Program exited successfully")
        break
    else:
        print("Invalid choice! Please try again.")
