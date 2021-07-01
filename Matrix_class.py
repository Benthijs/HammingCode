class matrix:
    """Represents a matrix with elements mod 2
    Attributes:
        mat: The list containing elements of the matrix
        dim: A touple representing dimension of the matrix
        rows: A list containing the rows of the matrix
        columns: A list containing the columns of the elements
    """
    def __init__(self, lst=None):
        #handles case when lst empty
        if lst == None:
            lst = []
        elif lst != []: # ensures the matrix has elements of mod 2
            for i in range(len(lst)):
                for j in range(len(lst[0])):
                    lst[i][j] %= 2
        self.mat = lst
        self.dim = (len(lst), len(lst[0]))
        self.rows = [lst[i][:] for i in range(self.dim[0])]
        self.columns = [[lst[i][j] for i in range(self.dim[0])] for j in range(self.dim[1])]
     
    def __eq__(self, other):
        return self.mat == other.mat

    def get(self, i, j):
        """For a matrix A returns the element on the ith row jth column"""
        return self.mat[i-1][j-1]
    
    def update(self, i, j, value):
        """For matrix update element in the ith row, jth column with value"""
        updated_matrix = self.mat
        updated_matrix[i-1][j-1] = value
        return matrix(updated_matrix)
    
    def transpose(self):
        """Returns the transpose of a matrix"""
        transpose = matrix(self.columns)
        return transpose
    
    def __str__(self):
        """Returns a string representation of the matrix for visualization"""
        out = '---\n'
        for row in self.mat:
            row = [str(i) for i in row]
            out += "[" + ' '.join(row) + ']\n'
        return out

    
    def __multlist(self, list1, list2):
        """A helper function for multiplication that computes the dot product
        of two vectors (represented by lists) in Z/2Z (elements are mod 2)
        list1: A list representing a row of a matrix
        list2: A list representing a column of a matrix"""
        if len(list1) == len(list2):
            return sum([list1[i]*list2[i] for i in range(len(list1))]) % 2

    def __mul__(self, other):
        """Returns the product of two matrices"""
        # Gaurdian code
        if not isinstance(other, matrix):
            raise TypeError("other not of type matrix")
        if self.dim[1] != other.dim[0]: # follows pylint no-else-raise
            raise ValueError("Matrices of incomplatible dimensions")  
        new_matrix = []
        for i in range(len(self.rows)):
            rows = []
            for j in range(len(other.columns)):
                rows.append(self.__multlist(other.columns[j], self.rows[i]))
            new_matrix.append(rows)
        return matrix(new_matrix)
    
    def __add__(self, other):
        """Returns the sum of two matrices"""
        #gaurdian code
        if(not isinstance(other, matrix)):
            raise TypeError("other is not of type matrix")
        elif(self.dim != other.dim):
            raise ValueError("Matrices not of compatible dimensions")
        if self.dim[1] == 1:
            new_matrix = [[0 for i in range(len(self.rows[0]))] for j in range(len(self.columns[0]))]
            for i in range(len(self.rows)):
                new_matrix[i][0] = (self.rows[i][0] + other.rows[i][0]) % 2
            return matrix(new_matrix)
        else:
            # addition of two matrices
            new_matrix = [[0 for i in range(len(self.rows[0]))] for j in range(len(self.columns[0]))]
            for i in range(len(other.rows)):
                for j in range(len(other.columns)):
                    # addition in mod 2
                    new_matrix[i][j] = (self.get(i, j) + other.get(i, j)) % 2
            return matrix(new_matrix)
    