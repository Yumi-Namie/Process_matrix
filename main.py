from process_matrix import process_matrix


""" This file is to test the function"""

# >> each list = one column
mtx = [[2,4,5,2],[4,6,2,3],[1,2,3,4],[5,6,7,8]] #square
# mtx = [[1,3,4,5],[5,6,7,0],[8,9,10,2]] # rectangular
# mtx = [[1,3,4],[5,6,7],[8,9,10],[2,3,4]] # rectangular
# mtx = [[1,3,4,5],[5,6,7,0],[8,9,10,2,5,6]] # no matrix
# mtx = [[1,2,1,2,3,2]] #just one column
# mtx = [['a','b','c','d']] #letters
# mtx = [[]]
# mtx = []



if __name__ == "__main__":

    process_matrix(mtx)
    