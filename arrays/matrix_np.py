import numpy as np

# in a numpy array, all element need to have the same number of parameters
numbers = np.array ([[4, 13, 16], [5, 7, 1], [8, 10, 15]])
print(numbers)

# above, function to count and manipulate numbers
min_nbr = numbers.min()
max_nbr = numbers.max()
sum_nbr = numbers.sum()
ave_nbr = numbers.mean()
det_nbr = numbers.std()
print("Min = ", min_nbr)
print("Max = ", max_nbr)
print("Sum = ", sum_nbr)
print("Ave = ", ave_nbr)
print("Det = ", det_nbr)
