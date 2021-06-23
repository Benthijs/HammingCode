import random

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
        if(lst == None):
            lst = []
        elif(lst != []): # ensures the matrix has elements of mod 2
            for i in range(len(lst)):
                for j in range(len(lst[0])):
                    lst[i][j] %= 2
        self.mat = lst
        self.dim = (len(lst), len(lst[0]))
        self.rows = [lst[i][:] for i in range(self.dim[0])]
        self.columns = [[lst[i][j] for i in range(self.dim[0])] for j in range(self.dim[1])]
        

    def get(self, i, j):
        """For a matrix A returns the element on the ith row jth column"""
        return self.mat[i-1][j-1]
    
    
    def __str__(self):
        """Returns a string representation of the matrix for visualization"""
        out = ''
        for row in self.mat:
            row = [str(i) for i in row]
            out += "[" + ' '.join(row) + '] \n'
        return out

    
    def __multlist(self, list1, list2):
        """A helper function for multiplication that computes the dot product
        of two vectors (represented by lists) in Z/2Z (elements are mod 2)
        list1: A list representing a row of a matrix
        list2: A list representing a column of a matrix"""
        if len(list1) == len(list2):
            return sum([list1[i]*list2[i] for i in range(len(list1))]) % 2

    # TODO handle errors, wrong types/incompatible sizes  
    def __mul__(self, other):
        """Returns the product of two matrices"""
        
        # Gaurdian code
        if(not isinstance(other, matrix)):
            raise TypeError("other not of type matrix")
        elif(self.dim[1] != other.dim[0]):
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
        
        # addition of two matrices
        new_matrix = [[0 for i in range(len(self.rows[0]))] for j in range(len(self.columns[0]))]
        for i in range(len(other.rows)):
            for j in range(len(other.columns[0])):
                # addition in mod 2
                new_matrix[i][j] = (self.get(i, j) + other.get(i, j)) % 2
        return new_matrix
    
vector = G * p


G = matrix([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0],[0, 0, 1, 0], [0, 0, 0, 1]])
G_T = matrix([[1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1]])
H = matrix([[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]])
p = matrix([[1], [0], [1], [1]])
R = matrix([[0,0,1,0,0,0,0], [0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]])
       

def omzet_bits(vector):
    """Switches a random number of bits"""
    prob = random.random() 
    bits = vector.mat 
    for i in range(len(bits)):
        if random.random() < prob:
            bits[i] = (bits[i] + 1) % 2
    return vector


#TODO check dimension of vector
def codeer(vector):
    """Codes the 4 bit message into one with three parity bits
        Attributes:
            vector: the 4-bit message"""
    return(G * vector)

def decodeer(vector):
    """Decodes the 7 bit vector into the original 4-bit message
        Attributes
            vector: the 7-bit hamming code with 3 parity and 4 data bits"""
    return R * vector

def controleer(vector):
    """Returns True if the message is sent correctly according to the parity bits"""
    
    #We moeten checken of de matrix H verminigvuldigd met een vector 0 is.
    controleer_vector = H * vector
    #Een vector bestaande uit 0 en 1 is 0 d.e.s.d.a. de som van de componenten 0 is.
    som_vector = 0
    
    for i in range(len(controleer_vector.rows)):
        som_vector += sum(controleer_vector.rows[i])
        if som_vector == 0:
            return True #Geen fout opgetreden
        else:
            return False #fout opgetreden
  
            
# TODO implement error correction function

def corrigeren(vector):
    """Returns the corrected vector based on the Hamming(7-4) code"""
    if(controleer(vector)):
        return vector
    # see error correction Hamming(7,4) wikipedia





    
    
    
    
    
    
    
    
    
    
    
    
    
    