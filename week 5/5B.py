class Node:
    """A Node in a Singly Linked List for the Stack"""
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        # In a linked list stack, the 'head' represents the 'top' of the stack
        self.top = None
        self.size = 0

    # 1. Push operation (Add element to the top)
    def push(self, data):
        new_node = Node(data)
        # New node points to the current top node
        new_node.next = self.top
        # Update the top pointer to the new node
        self.top = new_node
        self.size += 1
        print(f"Successfully pushed '{data}' onto the stack.")

    # 2. Pop operation (Remove element from the top)
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        
        popped_value = self.top.data
        # Move the top pointer to the next element
        self.top = self.top.next
        self.size -= 1
        print(f"Successfully popped '{popped_value}' from the stack.")
        return popped_value

    # 3. Peek operation (View top element without removing it)
    def peek(self):
        if self.is_empty():
            print("The stack is empty. Nothing to peek.")
            return None
        
        print(f"The top element (Peek) is: {self.top.data}")
        return self.top.data

    # 4. Count operation (Return total number of items)
    def count(self):
        return self.size

    # 5. Display operation (Show stack elements from top to bottom)
    def display(self):
        if self.is_empty():
            print("The stack is empty: Top -> None")
            return
        
        print("\n--- Current Stack (Top to Bottom) ---")
        temp = self.top
        is_first = True
        while temp is not None:
            if is_first:
                print(f"[{temp.data}] <- Top")
                is_first = False
            else:
                print(f"[{temp.data}]")
            temp = temp.next
        print("-------------------------------------")

    def is_empty(self):
        return self.top is None


# Main Menu-Driven Loop
def main():
    stack = StackLinkedList()

    while True:
        print("\n========================")
        print(" LINKED LIST STACK MENU")
        print("========================")
        print("1. Push (Add element)")
        print("2. Pop (Remove element)")
        print("3. Peek (View top element)")
        print("4. Count (Get total nodes)")
        print("5. Display stack elements")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice (1-6): "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if choice == 1:
            val = input("Enter the value to push onto the stack: ")
            stack.push(val)
            stack.display()

        elif choice == 2:
            stack.pop()
            stack.display()

        elif choice == 3:
            stack.peek()

        elif choice == 4:
            print(f"Total number of elements in stack: {stack.count()}")

        elif choice == 5:
            stack.display()

        elif choice == 6:
            print("Exiting stack program. Goodbye!")
            break
        else:
            print("Invalid option! Please pick a choice from 1 to 6.")


if __name__ == "__main__":
    main()
