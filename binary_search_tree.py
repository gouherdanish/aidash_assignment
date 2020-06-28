class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None

class BinaryProblem:

    def create_tree(self, arr, i, n):
        """
        Uses recursion to create a tree
        
        Input:  arr - user input array taken to form nodes of a tree
                i - index with respect to input array
                n - length of input array
        Output: node - object of type Node representing a binary tree grown out of input array
        """
        node = None
        if i < n:
            # Creating instance of root node with value
            node = Node(arr[i])

            # inserting left child
            node.left = self.create_tree(arr, 2*i+1, n)

            # inserting right child
            node.right = self.create_tree(arr, 2*i+2, n)

        return node
    
    def tree_are_mirror(self, tree1, tree2): 
        
        """
        Uses recursion to check if the tree1 is mirror of tree2
        
        Input: Binary trees tree1 and tree2 of object type Node
        Output: True - if trees are mirror
                False - if trees are not mirror
        """
        
        # Empty Trees
        if tree1 is None and tree2 is None: 
            return True
        
        # If tree1 is empty and tree2 is not, then not mirror
        if tree1 is None or tree2 is None: 
            return False
        
        # Three conditions for trees to be mirror
        # - 1) root node must be same
        # - 2) left sub-tree of tree1 must be same as right sub-tree of tree2
        # - 3) right sub-tree of tree1 must be same as left sub-tree of tree2
        return (tree1.data == tree2.data and 
                self.tree_are_mirror(tree1.left, tree2.right) and 
                self.tree_are_mirror(tree1.right , tree2.left)) 

    def convert_to_list(self, mystr):
        """
        Splits the user input based on space character
        input: mystr - string
        output: arr - list of strings
        """
        arr = mystr.split(" ")
        return arr


if __name__ == "__main__":
    try:
        bp = BinaryProblem()

        print("for printing the tree, just enter element separated by space from left to right.")
        print("if there is no data then use hyphen '-'")

        tree1 = input("for tree 1: ")
        tree1 = bp.convert_to_list(tree1)
        tree1 = bp.create_tree(tree1, 0, len(tree1))

        tree2 = input("for tree 2: ")
        tree2 = bp.convert_to_list(tree2)
        tree2 = bp.create_tree(tree2, 0, len(tree2))

        if bp.tree_are_mirror(tree1, tree2): print("Yes, trees are mirror")
        else: print("No, trees are not mirror")

    except Exception as e:
        print(e)