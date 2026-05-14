# 21. Write a menu driven program to read, add, subtract, multiply, divide, and
# transpose two matrices.
class Matrix:
    def __init__(self):
        self.matrix1 = []
        self.matrix2 = []

    def read(self):
        self.matrix1 = []
        self.matrix2 = []

        rows = int(input('How many rows does your first matrix have?: '))
        cols = int(input('How many colums does your first matrix have?: '))
        count = 0
        print('Type your numbers in the format: "2 3". Do not omit the space')
        while count < rows:
            row = input(f'Enter the digits in row {count+1}: ')
            values = list(map(float, row.split()))
            if len(values) != cols:
                print('Error! Values in row do not correspond to columns specified')
                continue
            self.matrix1.append(values)
            count+=1
        self.shape1 = (rows, cols)


        rows = int(input('How many rows does your second matrix have?: '))
        cols = int(input('How many colums does your seocnd matrix have?: '))
        count = 0
        print('Type your numbers in the format: "2 3". Do not omit the space')
        while count < rows:
            row = input(f'Enter the digits in row {count+1}: ')
            values = list(map(float, row.split()))
            if len(values) != cols:
                print('Error! Values in row do not correspond to columns specified')
                continue
            self.matrix2.append(values)
            count+=1
        self.shape2 = (rows, cols)


    def display(self):
        print('\nMatrix 1 =')
        for row in self.matrix1:
            print(row)

        print('\nMatrix 2 =')
        for rows in self.matrix2:
            print(rows)
        
    
    def add(self):
        if self.shape1 != self.shape2:
            print('Error! The two types of matrices inputed cannot be added. Input new matrices')
        else:
            result = []
            no_of_rows = self.shape1[0]
            no_of_cols = self.shape1[1]
            
            for i in range(no_of_rows):
                row_result = []
                for j in range(no_of_cols):
                    value = self.matrix1[i][j] + self.matrix2[i][j]
                    row_result.append(value)
                result.append(row_result)
            print('\nSum of the matrices = ')
            for row in result:
                print(row)

    def subtract(self):
        if self.shape1 != self.shape2:
            print('Error! The two types of matrices inputed cannot be added. Input new matrices')
            return
        else:
            result = []
            no_of_rows = self.shape1[0]
            no_of_columns = self.shape1[1]

            for i in range(no_of_rows):
                row_result = []
                for j in range(no_of_columns):
                    value = self.matrix1[i][j] - self.matrix2[i][j]
                    row_result.append(value)
                result.append(row_result)
            print('\nDifference of the matrices = ')
            for row in result:
                print(row)

    def multiply(self):
        rowsA, colsA = self.shape1
        rowsB, colsB = self.shape2
        if colsA != rowsB:
            print("\nError! Matrices cannot be multiplied \nThe number of columns in the first matrix must equal the number of rows in the second.")
            return
        else:
            result = []
            for i in range(rowsA):
                row_result = []
                for j in range(colsB):
                    total = 0
                    for k in range(colsA):
                        total += self.matrix1[i][k] * self.matrix2[k][j]
                    row_result.append(total)
                result.append(row_result)

            print('\nProduct of the matrices = ')
            for row in result:
                print(row)

    def divide(self):
        if self.shape1 != self.shape2:
            print('Error! The two types of matrices inputed cannot be added. Input new matrices')
            return
        else:
            result = []
            no_of_rows = self.shape1[0]
            no_of_columns = self.shape1[1]

            for i in range(no_of_rows):
                row_result = []
                for j in range(no_of_columns):
                    if self.matrix2[i][j] == 0:
                        print('Error! Division by zero!')
                        row_result.append('undefined')
                    else:
                        value = self.matrix1[i][j] / self.matrix2[i][j]
                        row_result.append(value)
                result.append(row_result)
            print('\nQuotient of element-wise division of the matrices = ')
            for row in result:
                print(row)

    def transpose(self):
        Matrix.display(self)
        choice = int(input('\nEnter the number of the matrix you want to transpose?: '))
        if choice == 1:
            rowsA, colsA = self.shape1
            result = []
            for j in range(colsA):
                new_row = []
                for i in range(rowsA):
                    new_row.append(self.matrix1[i][j])
                result.append(new_row)
            for row in result:
                print(row)
        elif choice == 2:
            rowsB, colsB = self.shape2
            result = []
            for j in range(colsB):
                new_row = []
                for i in range(rowsB):
                    new_row.append(self.matrix2[i][j])
                result.append(new_row)
            for row in result:
                print(row)
        else:
            print('Invalid input')

matrices = Matrix()

while True:
    actions = ['1. Read(enter your matrices here)', '2. Display', '3. Add', '4. Subtract', '5. Multiply', '6. Divide (Element-wise)', '7. Transpose', '8.Exit']
    for action in actions:
        print(action)
    chosen_action = int(input('\nEnter the number of the option of your choice:'))

    if chosen_action == 1:
        matrices.read()
    elif chosen_action == 2:
        matrices.display()
    elif chosen_action == 3:
        matrices.add()
    elif chosen_action == 4:
        matrices.subtract()
    elif chosen_action == 5:
        matrices.multiply()
    elif chosen_action == 6:
        matrices.divide()
    elif chosen_action == 7:
        matrices.transpose()
    elif chosen_action == 8:
        print('\nGoodbye!')
        break
    else:
        print('\nInvalid input')