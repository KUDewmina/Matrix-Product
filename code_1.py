while True:
    try : 
        # Asking the dimensions for two matrixes
        no_of_rows_1 = int(input("Enter number of rows of 1st matrix: "))
        no_of_columns_1 = int(input("Enter number of columns of 1st matrix: "))
        no_of_rows_2 = int(input("Enter number of rows of 2nd matrix: "))
        no_of_columns_2 = int(input("Enter number of columns of 2nd matrix: "))
    except ValueError :
        # Checking validity of inputs
        print("Please enter a valid number")
        break
    if no_of_rows_2 != no_of_columns_1 :
        # Checking if the two matrixes can be product
        print("Can't do a matrix product")
    else:
        break

matrix_1 = []
matrix_2 = []

# Getting the matrixes from user according to their dimensions
print("\nEnter elements for matrix 1 seperated by spaces")
for i in range(no_of_rows_1) :
    rows = list(map(int, input(f"--> Row {i+1} : ").split()))
    if len(rows) != no_of_columns_1 :
        print("Please enter a valid input")
        exit()
    matrix_1.append(rows)

print("\nEnter elements for matrix 2 seperated by spaces")
for i in range(no_of_rows_2) :
    rows = list(map(int, input(f"--> Row {i+1} : ").split()))
    if len(rows) != no_of_columns_2 :
        print("Please enter a valid input")
        exit()
    matrix_2.append(rows)

elements = []

try:
    for i in range(no_of_rows_1) : # Iterating through rows of first matrix
        for j in range(no_of_columns_2) : # Iterating through columns of second matrix
            result = 0
            for k in range(no_of_rows_2) : # Iterating through rows of second matrix
                result += matrix_1[i][k] * matrix_2[k][j]
            elements.append(result)
except IndexError:  # Checking if elements in matrixes are correct
    print("Your inputs may be wrong")
    exit()
    
row = []
final = []

point = 0
for val in elements :
    point += 1
    row.append(val)
    if point == no_of_columns_2 :
        final.append(row)
        row = []
        point = 0


print("\nFinal Matrix \n-------------")
print("[" +"\n".join(map(str, final)) + "]" + f"  --> This is a {no_of_rows_1} x {no_of_columns_2} matrix\n-------------------")
