# search with python function
name = ['John', 'Marrie', 'Anne']
i = name.index('John') #search for index with John's name
print(i)

# function to search

def searchList(toFind, List, sizeList):
    i = 0
    indexL = -1
    while i < sizeList:
        if List[i] == toFind: # node find
            indexL = i # keep index value
            i = sizeList + 1 # exit from loop
        i += 1 # if not find key value, keep searching
    return (indexL)

print(searchList('Anne', name, 3))
