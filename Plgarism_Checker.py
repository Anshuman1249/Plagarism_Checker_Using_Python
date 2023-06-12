#numpy is an open source library for working on multidimensional arrays
import numpy as np


# defining a function to compare the strings using levenshtein's algorithm
def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
 
# defining a zero matrix of size of first string * second string
    matrix = np.zeros ((size_x, size_y)) 
 
    for x in range(size_x):
        matrix [x, 0] = x # row aray with elements of x
    for y in range(size_y):
        matrix [0, y] = y # column array with elements of y
    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]: # if the alphabets at the postion is same
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
 
            else:           # if the alphabets at the position are different
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
 
    # returning the levenshtein distance i.e last element of the matrix
    return (matrix[size_x - 1, size_y - 1])
 

path2 = input("Enter the path of the first file to scan:\n")
path3 = input("Enter the path of the second file to scan:\n")
 
with open(path2, 'r') as file:
    data = file.read().replace('\n', '')
    str1=data.replace(' ', '')
 
with open(path3, 'r') as file:
    data = file.read().replace('\n', '')
    str2=data.replace(' ', '')
 
if(len(str1)>len(str2)):
    length=len(str1)
 
else:
    length=len(str2)
 
n = 100-round((levenshtein(str1,str2)/length)*100,2)
   
print("\n These two files have ", n,"% similarity")
