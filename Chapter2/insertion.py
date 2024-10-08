def insertionSort(arr : list) -> list:
    
    n = len(arr)
    
    for j in range(1,n):
        key = arr[j]
        i = j-1
        while (i >=0) and (key <= arr[i]):
            arr[i+1] = arr[i]
            i = i - 1
            
        arr[i+1] = key
    
    return arr



    
