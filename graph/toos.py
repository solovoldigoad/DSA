class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to perform inorder traversal
    def inorderTraversal(self, root, arr):
        # Base case
        if not root:
            return
        # Traverse left subtree
        self.inorderTraversal(root.left, arr)
        # Store current node data
        arr.append(root.data)
        # Traverse right subtree
        self.inorderTraversal(root.right, arr)

    # Function to merge two sorted lists
    def mergeArrays(self, arr1, arr2):
        # Initialize result
        merged = []
        # Initialize pointers
        i = j = 0
        # Merge until one list ends
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        # Add remaining elements
        merged.extend(arr1[i:])
        merged.extend(arr2[j:])
        return merged

    # Function to merge two BSTs
    def mergeBSTs(self, root1, root2):
        # Lists to store inorder traversals
        arr1, arr2 = [], []
        # Perform inorder traversals
        self.inorderTraversal(root1, arr1)
        self.inorderTraversal(root2, arr2)
        # Merge and return
        return self.mergeArrays(arr1, arr2)

# Driver code
if __name__ == "__main__":
    # Create first BST
    root1 = Node(3)
    root1.left = Node(1)



    # Print result
    print(*result)
