# define tree node structure
class TreeNode:
    # constructor
    def __init__(self, x: int):
        # value of the node
        self.val = x
        # left child reference
        self.left = None
        # right child reference
        self.right = None

# solution class
class Solution:
    # find inorder successor iteratively
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode | None':
        # initialize successor
        successor = None
        # traverse until root becomes None
        while root is not None:
            # when p is greater or equal, move right
            if p.val >= root.val:
                root = root.right
            # otherwise update successor and move left
            else:
                successor = root
                root = root.left
        # return successor (may be None)
        return successor

# inorder print helper
def print_in_order(root: 'TreeNode | None') -> None:
    # base case
    if root is None:
        return
    # traverse left
    print_in_order(root.left)
    # print node
    print(root.val, end=" ")
    # traverse right
    print_in_order(root.right)

# program entry
def main():
    # construct BST
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    # show inorder
    print("BST: ", end="")
    print_in_order(root)
    print()

    # target node p
    p = root.left.right

    # find successor
    solution = Solution()
    successor = solution.inorderSuccessor(root, p)

    # print result
    if successor is not None:
        print(f"Inorder Successor of {p.val} is: {successor.val}")
    else:
        print(f"Inorder Successor of {p.val} does not exist.")

# run main
if __name__ == "__main__":
    main()
