#Exercise 2.2-2


def SelectionSort(arr: list) -> list:
    
    n = len(arr)
    
    for i in range(0, n-1):
        
        index = i
        key = arr[i]
        
        for j in range(i+1, n):
            
            if arr[j] <= arr[i]:
                
                (arr[i], arr[j]) = (arr[j], arr[i])
                key = arr[i]
                index = j
                
    return arr



