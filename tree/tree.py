# This class defines a node in a Binary Search Tree
class TreeNode:
    # Constructor initializes the node with a value and sets children to None
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# This class is an iterator for traversing the BST
class BSTIterator:
    # Constructor initializes the iterator with root and traversal direction
    def __init__(self, root, isReverse):
        # A stack is used to store nodes while traversing
        self.stack = []
        # This flag tells whether we are doing normal inorder or reverse inorder
        self.reverse = isReverse
        # Push all nodes on one side into the stack
        self.pushAll(root)

    # This function checks if more nodes are left
    def hasNext(self):
        # If stack has elements, then nodes are still left
        return len(self.stack) > 0

    # This function returns the next node value in chosen order
    def next(self):
        # Pop the top node from stack
        tmpNode = self.stack.pop()
        # If reverse is False, move to right child
        if not self.reverse:
            self.pushAll(tmpNode.right)
        # If reverse is True, move to left child
        else:
            self.pushAll(tmpNode.left)
        # Return the value of node processed
        return tmpNode.val

    # Helper function to push nodes from current node down to left or right edge
    def pushAll(self, node):
        # Keep looping until node becomes None
        while node:
            # Add current node to stack
            self.stack.append(node)
            # If reverse is True, go to right child
            if self.reverse:
                node = node.right
            # Otherwise, go to left child
            else:
                node = node.left

# This class contains the solution logic
class Solution:
    # Function checks if BST has two nodes that sum to target k
    def findTarget(self, root, k):
        # If root is None, tree is empty, return False
        if not root:
            return False

        # Create two iterators: one from smallest, one from largest
        l = BSTIterator(root, False)
        r = BSTIterator(root, True)

        # Get first values
        i = l.next()
        j = r.next()

        # Loop until two values meet
        while i < j:
            # If sum is exactly k, return True
            if i + j == k:
                return True
            # If sum is smaller, move left iterator
            elif i + j < k:
                i = l.next()
            # If sum is larger, move right iterator
            else:
                j = r.next()
        # If no pair found, return False
        return False

# Function to print inorder traversal of BST
def printInOrder(root):
    # If root is None, stop recursion
    if not root:
        return
    # Visit left subtree
    printInOrder(root.left)
    # Print current node value
    print(root.val, end=" ")
    # Visit right subtree
    printInOrder(root.right)

# Driver code to test the program
if __name__ == "__main__":
    # Create a sample BST
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    # Print inorder traversal of tree
    print("Tree Initialized: ", end="")
    printInOrder(root)
    print()

    # Create solution object
    solution = Solution()

    # Define target sum
    target = 22

    # Check if pair exists
    exists = solution.findTarget(root, target)

    # Print result
    if exists:
        print(f"Pair with sum {target} exists.")
    else:
        print(f"Pair with sum {target} does not exist.")
