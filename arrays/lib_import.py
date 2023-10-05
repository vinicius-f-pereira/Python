# importa a lib and give a name
import numpy as np

# use np to assign value of an array
names = np.array (["John", "Marie", "Anne"])

print(names)

# variable to receive copy of a name
copy = names.copy()

# assign a name to index 0 of copy var.
copy[0] = "Nelson"

print(names)

print(copy)

# create a view
vision = names.view()

vision[0] = "Nelson"

print(names)

print(vision)

# use enumerate do print position in index and names like a list
for index, value in enumerate(names):
    print (index, value)
