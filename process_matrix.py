from functools import reduce
from transpose import transpose_repr
from verify import is_numerical, same_length

"""Please, take a look the readme.txt file and use the main.py file to test this program"""

def process_matrix(matrix):
    """ Return list of list with avarage.
    >> index represented for columns  by 'i' and for lines (elements) by 'j'
    """
    
    if type(matrix) == list: #if is a list
        if matrix == []:
            print('⚠️'+ '  ' +"It's Empty")
        if same_length(matrix):
            if is_numerical(matrix) == True: # if the elements are numbers
                processed_list = []
                for i, column in enumerate(matrix):
                    column_elements = []
                    for j, element in enumerate(column):
                        column_elements.append(process_element(i, j,matrix))
                    processed_list.append(column_elements)   
                print_matrix(matrix,processed_list) 
                return processed_list
    

        

def process_element(i, j, matrix):
    """
    Get the index of an elements and the list it is in. 
    Computes its average with its neighbors ans returns that everage
    """
    # get the list of neighbors 
    # i, j = get_neighbour_indices(i,columns, j, elements)
    index = get_neighbour_index(i,j,matrix)
    values = get_neighbour_values(index,matrix)

    # calculate your average
    average = get_average(values)
 
    # returns the final average
    return round(average,2)



def get_neighbour_index(i,j,matrix):
    """ 
    Getting all the neighbourhood (own index, upper index, down index, right index, left index.
    Even the imposible neighbours and than, using condicional to get just the posibles neighbours called selected_index
    """
    all_index = []
    n_columns = len(matrix)
    n_row = len(matrix[0])

    all_index.append((i-1,j)) #left-side
    all_index.append((i+1,j)) #right-side
    all_index.append((i,j+1)) #up
    all_index.append((i,j-1)) #down
    all_index.append((i,j)) #own-side

    selected_index = []
    for i,j in all_index:
        if i >= 0 and i<= (n_columns-1) and j >= 0 and j<= (n_row-1):
            selected_index.append((i,j))
    return selected_index

    

def get_neighbour_values(index, matrix):
    """ 
    Getting all the value of the existed neighbours + own value
    """
    values = []
    for i,j in index:
        values.append(matrix[i][j])
    return values
     


def get_average(numbers):
    """"
    Recives a list of numbers and returns their average
    """
    return reduce(lambda accum, b: accum + b, numbers, 0) / len(numbers)


def print_matrix(mtx,averages):
    print(f"\nMatrix: {mtx}\n")
    transpose_repr(mtx)
    print(f'\nAvarages: {averages}\n')
    transpose_repr(averages)



