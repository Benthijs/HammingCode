"""
We compare the runtime of the bitwise hamming implementation with the matrix
version
"""
import time
import hamming
import bitwise_hamming
import hamming_unittests


def hamming_functions(vector):
    """Uses the hamming functions to execute a couple of tasks"""
    hamming_vector = hamming.codeer(vector)
    hamming.decodeer(hamming_vector)
    # correct an error
    wrong_vector = hamming_unittests.omzet_bits(hamming_vector, 1)
    hamming.decodeer(wrong_vector)

def bitwise_hamming_functions(vector):
    """Executes the same tasks as in hamming_functions only uses the bitwise
    implementation"""
    hamming_vector = bitwise_hamming.bitwise_codeer(vector)
    bitwise_hamming.bitwise_decodeer(hamming_vector)
    # correct the vector
    wrong_vector = hamming_unittests.omzet_bits(hamming_vector, 1)
    bitwise_hamming.bitwise_decodeer(wrong_vector)

def compare(number = 10000):
    """Compares the two versions of the hamming code we created
        Attributes:
            number: number of times each function is executed
            """
    vector = hamming_unittests.random_vector()
    matrix_time = time.time()
    for _ in range(number):
        hamming_functions(vector)
    matrix_time = time.time() - matrix_time
    bitwise_time = time.time()
    for _ in range(number):
        bitwise_hamming_functions(vector)
    bitwise_time = time.time() - bitwise_time
    normalization = max([matrix_time, bitwise_time])
    print(("Time of execution for: \n  Matrix hamming code tasks: {:.2%} \n" +
           "  Bitwise hamming tasks: {:.2%}").format(matrix_time/normalization,
                                                   bitwise_time/normalization))
