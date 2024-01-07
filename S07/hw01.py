def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    
    s = [[num_rows] * num_columns for i in range(num_columns)]
    for i in range(0, num_rows):
        s[i][0] = i + 1
    for j in range(0, num_columns):
        s[0][j] = j + 1
    for i in range(1, num_rows):
        for j in range(1, num_columns):
            s[i][j] = operation(s[i][0], s[0][j])

    for i in range(0, num_rows):
        sep = " "
        for j in range(0, num_columns):
            if j == num_columns - 1:
                sep = ""
            print(s[i][j], end=sep)
        print()


print_operation_table(lambda x, y: x / y, 4, 4)
