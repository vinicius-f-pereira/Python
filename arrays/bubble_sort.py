# import python debugger to debug
# import pdb
# set trace to start debugging
# pdb.set_trace()
# create a function with 'Def' + function_name(parameters) to swap elements
def swap(seq, i):
    aux = seq[i]
    seq[i] = seq[i + 1]
    seq[i + 1] = aux

# array with numbers to sort
seq = [1, 15 , 22, 6, 7 ,19, 8, 3, 5 , 20]

# variable to verify if list is or not sorted
sort = 1

# while loop to verify sort variable
while sort:
    sort = 0
    i = 0
# for loop to swap elements in array
    for i in range(len(seq) - 1):
        if seq[i] > seq[i + 1]:
            swap(seq, i)
            print(seq)
            sort = 1


