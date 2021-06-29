from Matrix_class import matrix
import random


G = matrix([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0],[0, 0, 1, 0], [0, 0, 0, 1]])
G_T = matrix([[1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1]])
H = matrix([[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]])
p = matrix([[1], [0], [1], [1]])
R = matrix([[0,0,1,0,0,0,0], [0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]])
vector = G * p   
BASIS = [matrix([[1], [0], [0], [0], [0], [0], [0]]), matrix([[0], [1], [0], [0], [0], [0], [0]]), matrix([[0], [0], [1], [0], [0], [0], [0]]),
         matrix([[0], [0], [0], [1], [0], [0], [0]]), matrix([[0], [0], [0], [0], [1], [0], [0]]), matrix([[0], [0], [0], [0], [0], [1], [0]]),
         matrix([[0], [0], [0], [0], [0], [0], [1]]),]

vector_fout = matrix([[0], [1], [1], [0], [1], [1], [1]])


  

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
            vector: a matrix object representing the 4-bit message"""
    return(G * vector)

def decodeer(vector):
    """Decodes the 7 bit vector into the original 4-bit message
        Attributes
            vector: matrix object representing the 7-bit hamming code with 3 parity"""
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
  
        

def corrigeren(vector):
    """Returns the corrected vector based on the Hamming(7-4) code
    Attributes:
        vector: a hamming 7-vector"""
    for i in range(len(BASIS)):
        #Introduce som so we can check if the vector is correct later
        som = 0 
        #vector1 is the vector we get adding a standard basis vector to the vector with an error modulo 2
        #vector2 is the vector we get after checking if it is correct
        vector1 = matrix(vector + BASIS[i])
        vector2 = H * vector1
        #for loop to check if vector2 == 0
        for i in range(len(vector2.rows)):
            som += vector2.rows[i][0]
        #if som == 0 then vector2 == 0 so the error has been removed 
        if som == 0:
            return vector1
            # see error correction Hamming(7,4) wikipedia

# bitwise hamming(7-4) code