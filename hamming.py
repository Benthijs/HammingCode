from Matrix_class import matrix
import random

"----- Hamming 7, 4 --------"

G = matrix([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0],[0, 0, 1, 0], [0, 0, 0, 1]])
H = matrix([[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]])
R = matrix([[0,0,1,0,0,0,0], [0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]])

"----- Hamming 11,7 --------"

G2 = matrix([[1, 1, 0, 1, 1, 0, 1],
             [1, 0, 1, 1, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 1],
             [0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 1]])
H2 = matrix([[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
             [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]])
R2 = matrix([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

BASIS = [matrix([[1], [0], [0], [0], [0], [0], [0]]), matrix([[0], [1], [0], [0], [0], [0], [0]]), matrix([[0], [0], [1], [0], [0], [0], [0]]),
         matrix([[0], [0], [0], [1], [0], [0], [0]]), matrix([[0], [0], [0], [0], [1], [0], [0]]), matrix([[0], [0], [0], [0], [0], [1], [0]]),
         matrix([[0], [0], [0], [0], [0], [0], [1]]),]



def codeer(vector):
    """Codes the 4 bit message into one with three parity bits
        Attributes:
            vector: a matrix object representing the 4-bit message"""
    if vector.dim[0] == 4:
        return(G * vector)
    if vector.dim[0] == 7:
        return(G2 * vector)

def controleer(vector):
    """Returns True if the message is sent correctly according to the parity bits"""
    #We moeten checken of de matrix H verminigvuldigd met een vector 0 is.
    if vector.dim[0] == 7:
        controleer_vector = H * vector
    
        for i in range(len(controleer_vector.rows)):
            component = sum(controleer_vector.rows[i])
            if component != 0:
                return False #fout opgetreden
            return True #geen fout opgetreden
    if vector.dim[0] == 11:
        controleer_vector = H2 * vector
        for i in range(len(controleer_vector.rows)):
            component = sum(controleer_vector.rows[i])
            if component != 0:
                return False
            return True
        
def corrigeren(vector):
    """Returns the corrected vector based on the Hamming(7-4) code
    Attributes:
        vector: a hamming 7-vector"""
    if(controleer(vector)):
         return vector
    for i in range(len(BASIS)):
        #Introduce som so we can check if the vector is correct later
        som = 0 
        #vector1 is the vector we get adding a standard basis vector to the vector with an error modulo 2
        #vector2 is the vector we get after checking if it is correct
        vector1 = vector + BASIS[i]
        vector2 = H * vector1
        #for loop to check if vector2 == 0
        for i in range(len(vector2.rows)):
            som += vector2.rows[i][0]
        #if som == 0 then vector2 == 0 so the error has been removed 
        if som == 0:
            return vector1
            # see error correction Hamming(7,4) wikipedia
    raise ValueError("The given vector cannot be corrected")

def decodeer(vector):
    """Decodes the 7 bit vector into the original 4-bit message
        Attributes
            vector: matrix object representing the 7-bit hamming code with 3 parity"""
    if vector.dim[0] == 11:
        return R2 * vector
    if vector.dim[0] == 7:
        vector = corrigeren(vector)
        return R * vector
# bitwise hamming(7-4) code








