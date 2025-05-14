print("Running...")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in range(1, 11):
    print(number, end=" ")

print()

print("-----------------------------------------")
# Using inverse order
for number in range(len(numbers), -1, -1):
    print(number, end=" ")

print()

print("-----------------------------------------")
print("Matrix")
matrix = [
    [1,  2,  3,  4,  5,  6,  7],
    [8,  9,  10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34, 35]
]
#1 2 3 4 5 6 7 14 21 28 35 34 33 32 31 30 29 22 15 8 9 10 11 12 13 20 27 26 25 24 23 16 17 18 19
rows = len(matrix)
cols = len(matrix[0])
total_elements = rows * cols
sum = 0
print(rows, cols)

top = 0
right = cols - 1
bottom = rows - 1
left = 0

print(top)
print(right)
print(bottom)
print(left)

print("Running...")
while top <= bottom and left <= right:
    for col in range(left, right + 1):
        print(matrix[top][col], end=" ")
    top += 1

    for row in range(top, bottom + 1):
        print(matrix[row][right], end= " ")
    right -= 1

    if top <= bottom:
        for col in range(right, left - 1, -1):
            print(matrix[bottom][col], end= " ")
        bottom -= 1

    if left <= right:
        for row in range(bottom, top - 1, - 1):
            print(matrix[row][left], end= " ")
        left +=1

print()


