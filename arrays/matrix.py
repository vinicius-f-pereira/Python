import numpy as np

# declaration of a matrix of a market list
purchases = [["rice", 6], ["bean", 5, 1], ["meat", 50, 2]]
print(purchases)

# append still the same for this structure
purchases.append(["onion", 5, 1])
print(purchases)

# to append value in the array of index in position N
purchases[0].append(2)
print(purchases)

# to remove is the same
purchases.remove (["bean", 5 ,1])
print(purchases)

purchases.pop(2)
print(purchases)
