
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        node.height = 1 + max(
            self.height(node.left),
            self.height(node.right)
        )

    def right_rotate(self, y):
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        self.update_height(x)
        self.update_height(y)
        return y

    def insert_node(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self.insert_node(node.left, key)
        elif key > node.key:
            node.right = self.insert_node(node.right, key)
        else:
            return node

        self.update_height(node)
        balance = self.balance(node)

        # LL Case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # RR Case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # LR Case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # RL Case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete_node(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete_node(node.right, temp.key)

        self.update_height(node)
        balance = self.balance(node)

        # LL Case
        if balance > 1 and self.balance(node.left) >= 0:
            return self.right_rotate(node)

        # LR Case
        if balance > 1 and self.balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # RR Case
        if balance < -1 and self.balance(node.right) <= 0:
            return self.left_rotate(node)

        # RL Case
        if balance < -1 and self.balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def search(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self.search(node.left, key)

        return self.search(node.right, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

    def display(self, node):
        if node:
            print(node.key, end=" ")
            self.display(node.left)
            self.display(node.right)


tree = AVLTree()
root = None

while True:
    print("\n1.Insert  2.Delete  3.Search")
    print("4.Inorder  5.Preorder  6.Postorder")
    print("7.Display  8.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter value: "))
        root = tree.insert_node(root, key)

    elif choice == 2:
        key = int(input("Enter value to delete: "))
        if tree.search(root, key):
            root = tree.delete_node(root, key)
            print("Node deleted")
        else:
            print("Value not found")

    elif choice == 3:
        key = int(input("Enter value to search: "))
        if tree.search(root, key):
            print("Value found")
        else:
            print("Value not found")

    elif choice == 4:
        tree.inorder(root)
        print()

    elif choice == 5:
        tree.preorder(root)
        print()

    elif choice == 6:
        tree.postorder(root)
        print()

    elif choice == 7:
        tree.display(root)
        print()

    elif choice == 8:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
