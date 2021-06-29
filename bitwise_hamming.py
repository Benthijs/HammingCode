"""
Bitwise implementation of the Hamming(7-4) code
"""

from Matrix_class import matrix




def bitwise_controleer(vector):
    """Returns True if the parity bits are in accord with the data bits
        Attributes:
            vector: a hamming 7-vector"""
    if not isinstance(vector, matrix):
        raise TypeError("The argument should be of type matrix")
    if len(vector.mat) > 1: # ensures vector is of proper form
        vector = vector.transpose()
    if len(vector.mat) > 1:
        raise TypeError("Given is a matrix not a vector")
    if len(vector.mat[0]) != 7:
        raise ValueError("The vector should be of dimension 7")
    vector_list = vector.mat[0] # list of elements in the vector
    # assign the elements of the hamming vector to variables
    p_1,p_2,p_3 = vector_list[0], vector_list[1], vector_list[3]
    d_1,d_2,d_3,d_4 = vector_list[2], vector_list[4], vector_list[5],vector_list[6]
    print(vector_list)
    #check the parity bits
    if (d_1+d_2+d_4) % 2 != p_1:
        return False
    if (d_1+d_3+d_4) % 2 != p_2:
        return False
    if (d_2+d_3+d_4) % 2 != p_3:
        return False
    return True

def bitwise_codeer(vector):
    """Returns a hamming 7-vector
    Attributes:
        vector: a base 2 4-vector
    """
    if not isinstance(vector, matrix):
        raise TypeError("The argument should be of type matrix")
    if len(vector.mat) > 1: # ensures vector is of proper form
        vector = vector.transpose()
    if len(vector.mat) > 1:
        raise TypeError("Given is a matrix not a vector")
    if len(vector.mat[0]) != 4: # checks whether it is a vector of correct dimension
        raise ValueError("The vector should be of dimension 4")
    vector_list = vector.mat[0]
    # Retrieve the data bits
    d_1, d_2, d_3, d_4 = vector_list[0], vector_list[1], vector_list[2], vector_list[3]
    # Calculate the parity bits
    p_1 = d_1 + d_2 + d_4
    p_2 = d_1 + d_3 + d_4
    p_3 = d_2 + d_3 + d_4
    hamming_vector = matrix([[p_1,p_2,d_1,p_3,d_2,d_3,d_4]])
    return hamming_vector

def bitwise_corrigeren(vector):
    """Returns a corrected hamming 7-vector
    Attributes:
        vector: a hamming 7-vector
    """
    if bitwise_controleer(vector):
        return vector
    # check if changing a bit corrects the error
    vector_elementen = vector.mat[0]
    for i in range(7):
        nieuwe_elementen = vector_elementen.copy()
        nieuwe_elementen[i] += 1
        potentiele_vector = matrix([nieuwe_elementen])
        print(nieuwe_elementen, 'boo')
        if bitwise_controleer(potentiele_vector):
            return potentiele_vector
    raise ValueError("The given vector cannot be corrected")

def bitwise_decodeer(vector):
    """Returns a correct 4-vector
    Attributes:
        vector: a hamming 7-vector"""
    vector = bitwise_corrigeren(vector)
    elementen = vector.mat[0]
    data_vector = matrix([[elementen[2], elementen[4], elementen[5],
                          elementen[6]]]).transpose()
    return data_vector

c = matrix([[1,1,0,1]])
alpha = bitwise_codeer(c)
alpha=alpha.update(1,1, 0)
print(bitwise_decodeer(alpha))
