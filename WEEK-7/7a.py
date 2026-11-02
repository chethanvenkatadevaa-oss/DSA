
class BST:
    def __init__(self):
        self.tree = []

    # Insert Operation
    def insert(self):
        data = int(input("Enter element: "))

        if len(self.tree) == 0:
            self.tree.append(data)
        else:
            i = 0

            while i < len(self.tree):
                if self.tree[i] is None:
                    self.tree[i] = data
                    break
                elif data < self.tree[i]:
                    i = 2 * i + 1
                elif data > self.tree[i]:
                    i = 2 * i + 2
                else:
                    print("Duplicate elements not allowed")
                    return

                while i >= len(self.tree):
                    self.tree.append(None)

        print(data, "inserted successfully")

    # Search Operation
    def search(self):
        data = int(input("Enter element to search: "))
        i = 0

        while i < len(self.tree) and self.tree[i] is not None:
            if self.tree[i] == data:
                print("Element found")
                return

            elif data < self.tree[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2

        print("Element not found")

    # Find Minimum
    def find_min(self, i):
        while 2 * i + 1 < len(self.tree) and self.tree[2 * i + 1] is not None:
            i = 2 * i + 1
        return i

    # Delete Operation
    def delete(self):
        data = int(input("Enter element to delete: "))
        self._delete(0, data)

    def _delete(self, i, data):
        if i >= len(self.tree) or self.tree[i] is None:
            print("Element not found")
            return

        if data < self.tree[i]:
            self._delete(2 * i + 1, data)

        elif data > self.tree[i]:
            self._delete(2 * i + 2, data)

        else:
            left = 2 * i + 1
            right = 2 * i + 2

            if (left >= len(self.tree) or self.tree[left] is None) and \
               (right >= len(self.tree) or self.tree[right] is None):
                self.tree[i] = None

            elif left >= len(self.tree) or self.tree[left] is None:
                self.tree[i] = self.tree[right]
                self._delete(right, self.tree[right])

            elif right >= len(self.tree) or self.tree[right] is None:
                self.tree[i] = self.tree[left]
                self._delete(left, self.tree[left])

            else:
                min_index = self.find_min(right)
                self.tree[i] = self.tree[min_index]
                self._delete(min_index, self.tree[min_index])

            print("Element deleted successfully")

    # Inorder Traversal
    def inorder(self, i=0):
        if i < len(self.tree) and self.tree[i] is not None:
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    # Preorder Traversal
    def preorder(self, i=0):
        if i < len(self.tree) and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    # Postorder Traversal
    def postorder(self, i=0):
        if i < len(self.tree) and self.tree[i] is not None:
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")

    # Display Array
    def display(self):
        print("BST Array:", self.tree)


# Main Program
bst = BST()

while True:
    print("\n----- BINARY SEARCH TREE USING ARRAY -----")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bst.insert()
    elif choice == 2:
        bst.search()
    elif choice == 3:
        bst.delete()
    elif choice == 4:
        print("Inorder:", end=" ")
        bst.inorder()
        print()
    elif choice == 5:
        print("Preorder:", end=" ")
        bst.preorder()
        print()
    elif choice == 6:
        print("Postorder:", end=" ")
        bst.postorder()
        print()
    elif choice == 7:
        bst.display()
    elif choice == 8:
        print("Program exited successfully")
        break
    else:
        print("Invalid choice! Please try again.")
