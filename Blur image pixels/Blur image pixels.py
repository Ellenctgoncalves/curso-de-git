import sys
import math

def sum_arrays(array1, array2):
    new_array = []

    if len(array1) == len(array2):
        for i in range(len(array1)):
            new_array.append(array1[i] + array2[i])

    return new_array

if __name__ == "__main__":
    rows, cols = [int(i) for i in input().split()]
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            r, g, b = [int(k) for k in input().split()]
            row.append([r,g,b])
        matrix.append(row)

    for i in range(rows):
        for j in range(cols):
            amount = 1
            itself = matrix[i][j]
            pixel = itself

            if i != 0:
                above = matrix[i-1][j]
                pixel = sum_arrays(pixel, above)
                amount += 1
            if i != rows-1:
                below = matrix[i+1][j]
                pixel = sum_arrays(pixel, below)
                amount += 1
            if j != 0:
                left = matrix[i][j-1]
                pixel = sum_arrays(pixel, left)
                amount += 1
            if j != cols-1:
                right = matrix[i][j+1]
                pixel = sum_arrays(pixel, right)
                amount += 1

            print(pixel[0]//amount , pixel[1]//amount, pixel[2]//amount)
