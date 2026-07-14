# Node structure for
# the binary tree
class Node:
    # Constructor to initialize
    # the node with a value
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class to perform preorder traversal
class Solution:

    # Function to perform preorder traversal
    # of the tree and store values in 'arr'
    def preorder(self, root, arr):
        # If the current node is NULL
        # (base case for recursion), return
        if root is None:
            return
        # Push the current node's
        # value into the vector
        arr.append(root.data)
        # Recursively traverse
        # the left subtree
        self.preorder(root.left, arr)
        # Recursively traverse 
        # the right subtree
        self.preorder(root.right, arr)

    # Function to initiate preorder traversal
    # and return the resulting list
    def preOrder(self, root):
        # Create an empty list to
        # store preorder traversal values
        arr = []
        # Call the preorder traversal function
        self.preorder(root, arr)
        # Return the resulting list
        # containing preorder traversal values
        return arr

# Main function
if __name__ == "__main__":

    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting preorder traversal
    sol = Solution()
    result = sol.preOrder(root)

    # Displaying the preorder traversal result
    print("Preorder Traversal: ", end="")
    # Output each value in the
    # preorder traversal result
    for val in result:
        print(val, end=" ")
    print()
