# list question

'''
Write a Python function called remove_duplicates_sorted that
takes a sorted list of integers as input and removes duplicates in-place, 
without using any additional space. The function should return the modified 
list with unique elements only.
'''

import time

def remove_duplicates_sorted(lst: list[int]) -> list[int]:
	lst[:] = [lst[i] for i in range(len(lst)) if lst[i] not in lst[i+1:]]
	return lst


'''
Write a Python function called rotate_matrix_clockwise that takes a 
square matrix (list of lists) as input and rotates the matrix 90 degrees clockwise. 
The function should modify the input matrix in-place and return the rotated matrix.
'''

def rotate_matrix_clockwise(lst: list[list]) -> list[list]:
	matrix = []
	for i in range(len(lst)):
		temp = []
		for j in range(len(lst[0])):
			temp.append(lst[j][i])
		temp.reverse()
		matrix.append(temp)

	return  matrix
