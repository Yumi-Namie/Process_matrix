from texttable import Texttable


def nth_elements(matrix,index):
    """
    Recives one matrix and change the position of the elements accordin to the currently position
    """
    result =[]
    for i in matrix:
        result.append(i[index])
    return result



def transpose(matrix):
    """
    Recives one matrix and return a new one transposed
    """
    matrix_transposed = []
    try:
        for i in range(len(matrix[0])):
            matrix_transposed.append(nth_elements(matrix,i))
        return matrix_transposed
    except:
        print(f"Sorry, something wrong\n")


    
    
def transpose_repr(matrix):
    """
    # receives a matrix, transpose it and returns its table representation
    """
    try:
        table = Texttable()
        table.add_rows(matrix, header=False)
        print(table.draw())
    except:
        print("Oops, it's not possible to print the matrix\n")



