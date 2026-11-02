
class BinaryTree:
    def __init__(self):
        self.tree = []

    # Create Binary Tree
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            self.tree.append(data)

        print("Binary Tree created successfully")

    # Insert Operation
    def insert(self):
        data = int(input("Enter element to insert: "))
        self.tree.append(data)
        print("Node inserted successfully")

    # Search Operation
    def search(self):
        data = int(input("Enter element to search: "))

        if data in self.tree:
            print("Element found at index", self.tree.index(data))
        else:
            print("Element not found")

    # Delete Operation
    def delete(self):
        data = int(input("Enter element to delete: "))

        if data in self.tree:
            index = self.tree.index(data)
            last = self.tree.pop()

            if index < len(self.tree):
                self.tree[index] = last

            print("Node deleted successfully")
        else:
            print("Element not found")

    # Inorder Traversal
    def inorder(self, i=0):
        if i < len(self.tree):
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    # Preorder Traversal
    def preorder(self, i=0):
        if i < len(self.tree):
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    # Postorder Traversal
    def postorder(self, i=0):
        if i < len(self.tree):
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")

    # Display Operation
    def display(self):
        if len(self.tree) == 0:
            print("Tree is empty")
        else:
            print("Binary Tree Array:", self.tree)


# Main Program
bt = BinaryTree()

while True:
    print("\n----- BINARY TREE USING ARRAY -----")
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
        bt.inorder()
        print()
    elif choice == 6:
        print("Preorder:", end=" ")
        bt.preorder()
        print()
    elif choice == 7:
        print("Postorder:", end=" ")
        bt.postorder()
        print()
    elif choice == 8:
        bt.display()
    elif choice == 9:
        print("Program exited successfully")
        break
    else:
        print("Invalid choice! Please try again.")
