def check_sudoku():

# CASOS TEST
if __name__ == "__main__":
    correcto = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]

    assert check_sudoku(correcto) = True

    incorrecto1 = [[1, 2, 3, 4],
                   [2, 3, 1, 3],
                   [3, 1, 2, 3],
                   [4, 4, 4, 4]]
    
    assert check_sudoku(incorrecto1) = False

    incorrecto2 = [[1, 2, 3, 4],
                  [2, 3, 1, 4],
                  [4, 1, 2, 3],
                  [3, 4, 1, 2]]

    assert check_sudoku(incorrecto2) = False

    incorrecto3 = [[1, 2, 3, 4, 5],
                  [2, 3, 1, 5, 6],
                  [4, 5, 2, 1, 3],
                  [3, 4, 5, 2, 1],
                  [5, 6, 4, 3, 2]]
    
    assert check_sudoku(incorrecto3) = False

    incorrecto4 = [['a', 'b', 'c'],
                  ['b', 'c', 'a'],
                  ['c', 'a', 'b']]
    
    assert check_sudoku(incorrecto4) = False

    incorrecto5 = [[1, 1.5],
                  [1.5, 1]]
    
    assert check_sudoku(incorrecto5) = False

    incorrecto6 = [[1, 0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0, 1]]
    
    assert check_sudoku(incorrecto6) = False