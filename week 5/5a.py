class Stack:
    def __init__(self, capacity=10):
        """Initialize the stack with a fixed capacity using an array (list)."""
        self.capacity = capacity
        self.stack = []  # Array/list representation of the stack

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def is_full(self):
        """Check if the stack has reached its capacity limit."""
        return len(self.stack) >= self.capacity

    def push(self, element):
        """Add an element to the top of the stack (Push)."""
        if self.is_full():
            print(f"Stack Overflow! Cannot push '{element}'. The stack is full.")
        else:
            self.stack.append(element)
            print(f"Successfully pushed '{element}' onto the stack.")

    def pop(self):
        """Remove and return the top element of the stack (Pop)."""
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        else:
            removed_element = self.stack.pop()
            print(f"Successfully popped '{removed_element}' from the stack.")
            return removed_element

    def peek(self):
        """View the top element without removing it (Peek)."""
        if self.is_empty():
            print("The stack is empty. Nothing to peek.")
            return None
        else:
            top_element = self.stack[-1]
            print(f"The top element (Peek) is: {top_element}")
            return top_element

    def display(self):
        """Display all elements currently in the stack from top to bottom."""
        if self.is_empty():
            print("The stack is empty: []")
            return
        
        print("\n--- Current Stack (Top to Bottom) ---")
        # Print elements in reverse order to visually mimic a real-world stack
        for i in range(len(self.stack) - 1, -1, -1):
            if i == len(self.stack) - 1:
                print(f"[{self.stack[i]}] <- Top")
            else:
                print(f"[{self.stack[i]}]")
        print("-------------------------------------")


def main():
    # Take stack capacity from the user
    try:
        size = int(input("Enter the maximum capacity of the stack: "))
        if size <= 0:
            print("Capacity must be greater than 0. Setting default to 5.")
            size = 5
    except ValueError:
        print("Invalid input! Setting default capacity to 5.")
        size = 5

    my_stack = Stack(capacity=size)

    while True:
        print("\n========================")
        print("    STACK OPERATIONS")
        print("========================")
        print("1. Push (Add element)")
        print("2. Pop (Remove element)")
        print("3. Peek (View top element)")
        print("4. Display stack elements")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            val = input("Enter the value to push onto the stack: ")
            my_stack.push(val)
            my_stack.display()

        elif choice == 2:
            my_stack.pop()
            my_stack.display()

        elif choice == 3:
            my_stack.peek()

        elif choice == 4:
            my_stack.display()

        elif choice == 5:
            print("Exiting stack simulation. Goodbye!")
            break
        else:
            print("Invalid option! Please pick a choice from 1 to 5.")


if __name__ == "__main__":
    main()
