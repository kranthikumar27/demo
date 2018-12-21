'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.
    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def check_sudoku(elements):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if len(elements) < 81 or len(elements) > 81:
        return "Invalid input"
    n = 9
    [elements[i:i+n] for i in range(0, len(elements), n)]
    try:
        for i in range(len(elements)):
            temp = i.copy()
            list_1 = []
            int(temp.sort)
            if ''.join(temp) != '123456789':
                return "Invalid Sudoku:Duplicate values"
            for j in range(len(elements)):
                list_1.append(elements[j][i])
            list_1.sort()
            if ''.join(list_1) != '123456789':
                return "Invalid Sudoku:Duplicate values"
    except:
            return "Invalid Sudoku:Duplicate values"




def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    elements = str(input())
    print(check_sudoku(elements))

if __name__ == '__main__':
    main()
