Hey there!

This challenge is from the Bootcamp KeepCoding:

Basically is to receive one MATRIX (list of lists) and
calculate the average of each element in this matrix according with their neighbours.
And than, return the new matrix with all those averages.

>> Neighbours: numbers those share one edge.
We could say that there's three kinds of elements: corners, interiors and borders.
- corners have just two neighbours
- borders have three neighbours
- interior have four neighbours
>> Avarages: (own_value + neigbours_values) / ((itself) + neighbours)



>> Please, to test the function, use the file named as main.py << 



Example:

mtx = [[2,4,5,2],[4,6,2,3],[1,2,3,4],[5,6,7,8]]

process_matrix(mtx)

Matrix: [[2, 4, 5, 2], [4, 6, 2, 3], [1, 2, 3, 4], [5, 6, 7, 8]]

+---+---+---+---+
| 2 | 4 | 5 | 2 |
+---+---+---+---+
| 4 | 6 | 2 | 3 |
+---+---+---+---+
| 1 | 2 | 3 | 4 |
+---+---+---+---+
| 5 | 6 | 7 | 8 |
+---+---+---+---+


Avarages: [[3.33, 4.25, 3.25, 3.33], [3.25, 3.6, 3.8, 2.75], [3.0, 3.6, 3.6, 4.5], [4.0, 5.0, 6.0, 6.33]]

+-------+-------+-------+-------+
| 3.330 | 4.250 | 3.250 | 3.330 |
+-------+-------+-------+-------+
| 3.250 | 3.600 | 3.800 | 2.750 |
+-------+-------+-------+-------+
| 3     | 3.600 | 3.600 | 4.500 |
+-------+-------+-------+-------+
| 4     | 5     | 6     | 6.330 |
+-------+-------+-------+-------+



