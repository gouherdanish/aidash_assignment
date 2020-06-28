class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None

class BinaryProblem:
    def __init__(self):
        pass

    def create_tree(self, arr, root, i, n):
        if i < n:
            root = Node(arr[i])

            # insert left child
            root.left = self.create_tree(arr, root.left, 2*i+1, n)

            # insert right child
            root.right = self.create_tree(arr, root.right, 2*i+2, n)

        return root
    
    def tree_are_mirror(self, tree1, tree2): 
        
        if tree1 is None and tree2 is None: 
            return True
        
        if tree1 is None or tree2 is None: 
            return False
        
        return (tree1.data == tree2.data and 
                self.tree_are_mirror(tree1.left, tree2.right) and 
                self.tree_are_mirror(tree1.right , tree2.left)) 

    def convert_to_list(self, mystr):
        arr = mystr.split(" ")
        return arr


if __name__ == "__main__":
    try:
        bp = BinaryProblem()

        print("for printing the tree just write element, space seperated left to right.")
        print("if there is no data then use hiphen '-'")

        tree1 = input("for tree 1: ")
        tree1 = bp.convert_to_list(tree1)
        tree1 = bp.create_tree(tree1, None, 0, len(tree1))

        tree2 = input("for tree 2: ")
        tree2 = bp.convert_to_list(tree2)
        tree2 = bp.create_tree(tree2, None, 0, len(tree2))

        if bp.tree_are_mirror(tree1, tree2): print("tree are mirror")
        else: print("not mirror")

    except Exception as e:
        print(e)