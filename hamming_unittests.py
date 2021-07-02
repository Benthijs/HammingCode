"""
Unittests for the Hamming(7,4) code the bitwise Hamming(7,4) code and the
matrix class
"""
import unittest
import random
import hamming
import bitwise_hamming
from Matrix_class import matrix



def omzet_bits(vector, number_bits):
    """Switches a random number of bits in a vector
        Attributes:
            vector: A n-vector
            number_bits: the number of bits to be changed"""
    if len(vector.mat)>1:
        vector = vector.transpose()
    if len(vector.mat)>1:
        raise TypeError("vector cannot be a matrix")
    vector_list = vector.mat[0].copy()
    choices = list(range(0,len(vector.mat[0])))
    random.shuffle(choices)
    for _ in range(number_bits):
        vector_list[choices[-1]] = (vector_list[choices[-1]] + 1) % 2
        choices.pop(-1)
    vector = matrix([vector_list])
    return vector.transpose()

def random_vector():
    """Returns a random four-vector"""
    return matrix([[random.choice([0,1]) for i in range(4)]]).transpose()

def random_matrix():
    """Returns a random matrix"""
    cols = int(random.random() * 10) + 1
    rows = int(random.random() * 10) + 1
    els = [0,1]
    the_matrix = [[random.choice(els) for i in range(cols)] for j in
                  range(rows)]
    return matrix(the_matrix)


class TestHammingMethods(unittest.TestCase):
    """Unittests for the hamming.py functions"""
    def test_codeer(self):
        """Test that a 4-vector is encoded correctly"""
        # the four vector to test on
        four_vector = [1,0,1,0]
        # the solution we should obtains
        the_solution = [1,0,1,1,0,1,0]
        # the solution found by the codeer function
        encoded_four_vector = hamming.codeer(matrix([four_vector]).transpose())
        # checks if the solution is correct
        self.assertEqual(encoded_four_vector,
                        matrix([the_solution]).transpose())

    def test_controleer(self):
        """Test that the controleer function recognizes an incorrect 7-vector"""
        # create an arbitrary base 2 four-vector
        four_vector = random_vector()
        # convert it to a hamming-vector
        hamming_vector = hamming.codeer(four_vector)
        # create a random error
        wrong_hamming_vector = omzet_bits(hamming_vector, 1)
        # check that wrong hamming-vector is indeed wrong
        self.assertFalse(hamming.controleer(wrong_hamming_vector))
        # check that the hamming_vector is indeed correct
        self.assertTrue(hamming.controleer(hamming_vector))

    def test_decodeer(self):
        """Test that a random 4-vector is equal to the decoded hamming 7-vector
        thus also tests corrigeren and controleer"""
        four_vector = random_vector()
        # checks that a random four vector that is encoded then decoded correct is
        self.assertEqual(four_vector, hamming.decodeer(hamming.codeer(
            four_vector)))

    def test_corrigeren(self):
        """Test that a given number of vectors are correctly corrected uses the
        function omzet_bits to change a given number of bits at random"""
        four_vector = random_vector()
        # encode a random 4-vector
        hamming_vector = hamming.codeer(four_vector)
        # create a random error
        wrong_hamming_vector = omzet_bits(hamming_vector, 1)
        self.assertEqual(hamming.corrigeren(wrong_hamming_vector),
                         hamming_vector)

class TestBitwiseHamming(unittest.TestCase):
    """Unittests for the bitwise_hamming.py functions"""
    def test_bitwise_codeer(self):
        """Test that a 4-vector is encoded correctly"""
        # the four vector to test on
        four_vector = [1,0,1,0]
        # the solution we should obtains
        the_solution = [1,0,1,1,0,1,0]
        # the solution found by the codeer function
        encoded_four_vector = bitwise_hamming.bitwise_codeer(matrix(
            [four_vector]).transpose())
        # checks if the solution is correct
        self.assertEqual(encoded_four_vector, matrix([the_solution]
                                                     ).transpose())

    def test_bitwise_controleer(self):
        """Test that the controleer function recognizes an incorrect 7-vector"""
        # create an arbitrary base 2 four-vector
        four_vector = random_vector()
        # convert it to a hamming-vector
        hamming_vector = bitwise_hamming.bitwise_codeer(four_vector)
        # create a random error
        wrong_hamming_vector = omzet_bits(hamming_vector, 1)
        # check that wrong hamming-vector is indeed wrong
        self.assertFalse(bitwise_hamming.bitwise_controleer(
            wrong_hamming_vector))
        # check that the hamming_vector is indeed correct
        self.assertTrue(bitwise_hamming.bitwise_controleer(hamming_vector))

    def test_bitwise_decodeer(self):
        """Test that a random 4-vector is equal to the decoded hamming 7-vector
        thus also tests corrigeren and controleer"""
        four_vector = random_vector()
        # checks that a random four vector that is encoded then decoded correct is
        self.assertEqual(four_vector, bitwise_hamming.bitwise_decodeer(
            bitwise_hamming.bitwise_codeer(four_vector)))

    def test_bitwise_corrigeren(self):
        """Test that a given number of vectors are correctly corrected uses the
        function omzet_bits to change a given number of bits at random"""
        four_vector = random_vector()
        # encode a random 4-vector
        hamming_vector = bitwise_hamming.bitwise_codeer(four_vector)
        # create a random error
        wrong_hamming_vector = omzet_bits(hamming_vector, 1)
        self.assertEqual(bitwise_hamming.bitwise_corrigeren(
            wrong_hamming_vector), hamming_vector)


class TestMatrixClass(unittest.TestCase):
    """Unittests for the matrix class"""
    def test_get(self):
        """Tests if the matrix get function works properly"""
        test_matrix = matrix([[0,0,0],[0,1,0],[0,0,0]])
        self.assertEqual(1, test_matrix.get(2,2))

    def test_update(self):
        """Tests if the matrix update function works properly"""
        test_matrix = matrix([[1,0,1,0], [1,0,0,1], [1,0,0,0], [0,1,1,1]])
        # the matrix that the test_matrix should become after the given update
        correct_matrix = matrix([[1,0,1,0],[1,0,0,1],[1,0,0,0],[0,1,1,0]])
        self.assertEqual(test_matrix.update(4,4,0), correct_matrix)

    def test_transpose(self):
        """Tests if the matrix tranpose function works as expected"""
        the_matrix = random_matrix()
        # check if the transpose of the transpose of a matrix is itself
        self.assertEqual(the_matrix, the_matrix.transpose().transpose())

    def test_add(self):
        """Tests if the matrix addition works as expected"""
        the_matrix = random_matrix()
        zero_matrix = matrix([[0 for i in range(the_matrix.dim[1])]
                       for j in range(the_matrix.dim[0])])
        # check that the addition of the matrix with itself is the zero matrix
        self.assertEqual((the_matrix + the_matrix), zero_matrix)

    def test_mul(self):
        """Tests if matrix multiplication works as expected"""
        vector = random_vector().transpose()
        identity_matrix = matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        # check that the identity time a vector is the vector
        self.assertEqual(vector * identity_matrix, vector)


if __name__ == '__main__':
    unittest.main()
    