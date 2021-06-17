# HammingCode
class matrix:
    
    def __init__(self, lst):
        self.mat = lst
        self.dim = (len(lst), len(lst[0]))
        self.rows = [lst[i][:] for i in range(self.dim[0])]
        self.columns = [[lst[i][j] for i in range(self.dim[0])] for j in range(self.dim[1])]
        

    def get(self, i, j):
        return self.mat[i-1][j-1]

    
    def __multlist(self, list1, list2):
        if len(list1) == len(list2):
            return sum([list1[i]*list2[i] for i in range(len(list1))])

        
    def mult(self, other):
        new_matrix = []
        for i in range(len(self.rows)):
            rows = []
            for j in range(len(other.columns)):
                rows.append(self.__multlist(other.columns[j], self.rows[i]))
            new_matrix.append(rows)
        return new_matrix
    

    def add(self, other):
        new_matrix = [[0 for i in range(len(self.rows[0]))] for j in range(len(self.columns[0]))]
        for i in range(len(other.rows)):
            for j in range(len(other.columns[0])):
                new_matrix[i][j] = self.get(i, j) + other.get(i, j)
        return new_matrix
        
        
  
