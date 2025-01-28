"""Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

Prints the entire matrix row by row.
Prints the sum of each row in the matrix."""

rows = int(input("Enter the number of Rows: "))

matrix = []

for i in range(rows):
    row=[int(num) for num in input(f"Enter the number of Rows{i+1}: ").split( )]
    matrix.append(row)
print(matrix)

