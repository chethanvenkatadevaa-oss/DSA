
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
