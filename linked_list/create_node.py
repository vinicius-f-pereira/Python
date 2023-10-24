# creating node class and constructor
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# creating LinkedList class and constructor and a function do print
class LinkedList:
    def __init__(self, head = None):
        self.head = head

# function to print
    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

# search in linked list
def search(self, value):
    current = self.head
    if current.key == value:
        return current
    while current.next != None:
        current = current.next
        if current.key == value
            return current
    return None

# insert at start of a linked list
def insertStart(self, newNode):
    newNode.next = self.head
    self.head = newNode

# insert at end of a linked list
def insertEnd(self, newNode):
    current = self.head
    if current:
        while current.next:
            current = current.next
        current.next = newNode
    else:
        self.head = newNode

# remove from a linked list
def removeFromList(self, value):
    current = self.head
    if current == None:
        return None
    if current.key = value:
        self.head == current.next
        return 0
prevNode = current
current = current.next
    while (current != None):
        if current.key == value:
            prevNode.next = current.next
            return value
        else:
            prevNode = current
            current = current.next
    return -1
