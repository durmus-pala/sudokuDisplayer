sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
print("----------------------")
for i in range(len(sudoku)):
    if (i % 3 == 0) and (i != 0):
        print("---------------------")
    for j in range(len(sudoku)):
        if (j % 3 == 0) and (j != 0):
            print("|", end = " ")
        print(sudoku[i][j], end= " ")  
    print()
print("---------------------")
    

        

    
            
        
        
