def get_rows_and_cols():
    row_by_col_list = input().split()
    return row_by_col_list


def get_matrix(rows, cols):
    matrix_list = [input().split()[:cols] for y in range(rows)]
    return matrix_list


def get_rows(row_by_col_list):
    num_rows = int(row_by_col_list[0])
    return num_rows


def get_cols(row_by_col_list):
    num_cols = int(row_by_col_list[1])
    return num_cols


def print_matrix(n):
    for row in n:
        print(" ".join(row))


# print_matrix(matrix_a)

# defining second matrix
# row_by_col_list_b = input().split()
# print(row_by_col_list_b)

# num_rows_b = int(row_by_col_list_b[0])
# num_cols_b = int(row_by_col_list_b[1])

# matrix_b = [input().split()[:num_cols_b] for i in range(num_rows_b)]

# print(matrix_b)

# print_matrix(matrix_b)
def sum_matrices():
    print("Enter size of first matrix:")
    row_by_col_list_a = get_rows_and_cols()
    rows_a = get_rows(row_by_col_list_a)
    cols_a = get_cols(row_by_col_list_a)
    print("Enter first matrix:")
    matrix_a = get_matrix(rows_a, cols_a)
    # print(matrix_a)

    print("Enter size of second matrix:")
    row_by_col_list_b = get_rows_and_cols()
    rows_b = get_rows(row_by_col_list_b)
    cols_b = get_cols(row_by_col_list_b)
    print("Enter second matrix:")
    matrix_b = get_matrix(rows_b, cols_b)
    # print(matrix_b)

    new_matrix = []
    counter = 0
    if row_by_col_list_a == row_by_col_list_b:
        for i in matrix_a:
            new_matrix.append([])
            for j in i:
                new_matrix[counter].append(j)
            counter += 1
        counter = 0
        for i in matrix_b:
            counter_1 = 0
            for j in i:
                new_matrix[counter][counter_1] = str(float(j) + float(new_matrix[counter][counter_1]))
                counter_1 += 1
            counter += 1
        # print(new_matrix)
        print("The result is:")
        print_matrix(new_matrix)
    else:
        print("The operation cannot be performed.")
    main_menu()


def multiply_by_constant():
    print("Enter size of matrix:")
    matrix_size = get_rows_and_cols()
    rows = get_rows(matrix_size)
    cols = get_cols(matrix_size)
    print("Enter matrix:")
    matrix = get_matrix(rows, cols)

    constant = float(input("Enter constant:"))
    new_matrix = []
    counter = 0
    for i in matrix:
        new_matrix.append([])
        for j in i:
            new_matrix[counter].append(str(float(j) * constant))
        counter += 1
    print("The result is:")
    print_matrix(new_matrix)
    main_menu()


def multiply_matrices():
    print("Enter size of first matrix:")
    row_by_col_list_a = get_rows_and_cols()
    rows_a = get_rows(row_by_col_list_a)
    cols_a = get_cols(row_by_col_list_a)
    print("Enter first matrix:")
    matrix_a = get_matrix(rows_a, cols_a)
    # print(matrix_a)

    print("Enter size of second matrix:")
    row_by_col_list_b = get_rows_and_cols()
    rows_b = get_rows(row_by_col_list_b)
    cols_b = get_cols(row_by_col_list_b)
    print("Enter second matrix:")
    matrix_b = get_matrix(rows_b, cols_b)
    # print(matrix_b)

    col_matrix_b = trans_main_diag(matrix_b, cols_b)
    # print(col_matrix_b)

    new_matrix = []
    if cols_a != rows_b:
        print("The operation cannot be performed.")
    else:
        for i in range(rows_a):
            new_matrix.append([])
            # new matrix has same number of rows as matrix a so we append empty row to new matrix for each row in a
            for k in range(cols_b):
                new_element = 0
                for j in range(cols_a):
                    new_element += float(matrix_a[i][j]) * float(col_matrix_b[k][j])
                new_matrix[i].append(str(new_element))
                # print(new_matrix)

        # print(new_matrix)
        print("The result is:")
        print_matrix(new_matrix)

    main_menu()


def trans_main_diag(row_matrix, num_of_cols):
    col_matrix = []
    for col in range(num_of_cols):
        col_matrix.append([])
    for j in range(num_of_cols):
        for i in row_matrix:
            col_matrix[j].append(i[j])
    return col_matrix


def trans_side_diag(row_matrix, num_of_cols):
    new_matrix = []
    for col in range(num_of_cols):
        new_matrix.append([])
    counter = 0
    for i in range(num_of_cols)[::-1]:
        for j in row_matrix[::-1]:
            new_matrix[counter].append(j[i])
        counter += 1
    return new_matrix


def trans_vert_line(row_matrix, num_of_rows, num_of_cols):
    new_matrix = []
    for row in range(num_of_rows):
        new_matrix.append([])
    counter = 0
    for i in range(num_of_rows):
        for j in range(num_of_cols)[::-1]:
            new_matrix[counter].append(row_matrix[i][j])
        counter += 1
    return new_matrix


def trans_hori_line(row_matrix, num_of_rows, num_of_cols):
    new_matrix = []
    for row in range(num_of_rows):
        new_matrix.append([])
    counter = 0
    for i in range(num_of_rows)[::-1]:
        for j in range(num_of_cols):
            new_matrix[counter].append(row_matrix[i][j])
        counter += 1
    return new_matrix


def transpose_menu():
    print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    choice = int(input("Your choice:"))

    print("Enter matrix size:")
    matrix_size = get_rows_and_cols()
    rows = get_rows(matrix_size)
    cols = get_cols(matrix_size)
    print("Enter matrix:")
    matrix = get_matrix(rows, cols)

    if choice == 1:
        result = trans_main_diag(matrix, cols)
    elif choice == 2:
        result = trans_side_diag(matrix, cols)
    elif choice == 3:
        result = trans_vert_line(matrix, rows, cols)
    else:
        result = trans_hori_line(matrix, rows, cols)
    print("The result is:")
    print_matrix(result)
    main_menu()


def calc_determinant(matrix):
    if len(matrix) == 1:
        det = float(matrix[0][0])
        return det
    elif len(matrix) == 2:  # recall that matrix is a list of the rows which are also lists
        det = float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
        return det
    else:
        det = 0
        counter = 0
        sub_matrix_0 = matrix[1::]
        # print(sub_matrix_0)
        for i in range(len(matrix)):
            sub_matrix_1 = trans_main_diag(sub_matrix_0, len(matrix))
            # print(sub_matrix_1)
            del(sub_matrix_1[counter])
            sub_matrix_2 = trans_main_diag(sub_matrix_1, len(matrix) - 1)
            # print(sub_matrix_2)
            # print(calc_determinant(sub_matrix_2))
            # print(matrix[0][counter])
            # print((-1)**counter)
            det += (-1)**counter * float(matrix[0][counter]) * calc_determinant(sub_matrix_2)
            # print(det)
            counter += 1
        return det


def cofact_matrix(matrix):
    new_matrix = []
    for row in matrix:
        new_matrix.append([])
    counter = 0
    for i in range(len(matrix)):
        dummy_matrix = matrix.copy()
        del(dummy_matrix[counter])
        # print(dummy_matrix)
        # print(matrix)
        counter_1 = 0
        for j in range(len(matrix)):
            sub_matrix_1 = trans_main_diag(dummy_matrix, len(matrix))
            # print(sub_matrix_1)
            del(sub_matrix_1[counter_1])
            sub_matrix_2 = trans_main_diag(sub_matrix_1, len(matrix) - 1)
            # print(sub_matrix_2)
            minor = calc_determinant(sub_matrix_2)
            new_matrix[counter].append(float(minor) * (-1)**(counter + counter_1))
            # print(new_matrix)
            counter_1 += 1
        counter += 1
    return new_matrix


def get_inverse(matrix):
    if len(matrix) == 1:
        inverse = [[]]
        inverse[0].append(str(1/float(matrix[0][0])))
        return inverse
    else:
        cofactor_matrix = cofact_matrix(matrix)
        transp_cofact_matrix = trans_main_diag(cofactor_matrix, len(cofactor_matrix))
        # print(transp_cofact_matrix)
        determinant = calc_determinant(matrix)
        # print(determinant)
        if determinant == 0:
            print("This matrix doesn't have an inverse.")
            main_menu()
        else:
            recip_determinant = 1/determinant
            inverse = []
            counter = 0
            for i in transp_cofact_matrix:
                inverse.append([])
                for j in i:
                    inverse[counter].append(str(float(j) * recip_determinant))
                counter += 1
            return inverse


def main_menu():
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
    choice = int(input("Your choice:"))

    if choice == 1:
        sum_matrices()
    elif choice == 2:
        multiply_by_constant()
    elif choice == 3:
        multiply_matrices()
    elif choice == 4:
        transpose_menu()
    elif choice == 5:
        print("Enter matrix size:")
        matrix_size = get_rows_and_cols()
        rows = get_rows(matrix_size)
        cols = get_cols(matrix_size)
        print("Enter matrix:")
        matrix = get_matrix(rows, cols)
        print("The result is:")
        print(calc_determinant(matrix))
        main_menu()
    elif choice == 6:
        print("Enter matrix size:")
        matrix_size = get_rows_and_cols()
        rows = get_rows(matrix_size)
        cols = get_cols(matrix_size)
        print("Enter matrix:")
        matrix = get_matrix(rows, cols)
        # print(matrix)
        print("The result is:")
        inverse_matrix = (get_inverse(matrix))
        print_matrix(inverse_matrix)
        main_menu()


main_menu()
