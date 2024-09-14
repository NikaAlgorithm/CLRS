"""
    Exercise 2.1-3
"""


def linearSearch(lst: list, value: int) -> int:
    
    for i in range(len(lst)):
        
        if lst[i] == value :
            return i + 1
    
    return -1


