class MatrixProblem:
    def __init__(self):
        self.spiral_matrix = []
        
    def run(self, matrix, m, n, i, j):
        if i >= m or j >=n: return

        # print first row
        for x in range(i, n):
            self.spiral_matrix.append(matrix[i][x])
        
        # print last column
        for x in range(i+1, m):
            self.spiral_matrix.append(matrix[x][n-1])
        
        # print last row if it is not same as first one
        if m-1 != i:
            for x in range(n-2, j-1, -1):
                self.spiral_matrix.append(matrix[m-1][x])
        
        # print first column if last one is not same
        if n-1 != j:
            for x in range(m-2, i, -1):
                self.spiral_matrix.append(matrix[x][j])
        
        # call recursion with the inside matrix
        self.run(matrix, m-1, n-1, i+1, j+1)

if __name__ == "__main__":
    try:
        m = int(input("Enter total no of rows: "))
        n = int(input("Enter total no of columns: "))

        print("enter all the element seperated by space\n")
        matrix = []
        for i in range(m):
            mystr = input("for row {}: ".format(i+1))
            mylist = mystr.split(" ")
            if len(mylist) != n: raise Exception("there should be exactly {} element".format(n))
            
            matrix.append(mylist)
        
        print(matrix)

        # init the class
        mp = MatrixProblem()
        mp.run(matrix, m, n, 0, 0)
        print(mp.spiral_matrix)
        
    except Exception as e:
        print(e)