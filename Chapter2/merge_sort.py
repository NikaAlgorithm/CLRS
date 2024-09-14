def Merge(arr, s, m, e):
    
    n1 = m - s + 1
    n2 = e - m
    
    left = [0] * n1
    right = [0] * n2
    
    for i in range(n1):
        left[i] = arr[s + i]
        
    for j in range(n2):
        right[j] = arr[m + j + 1]
        
        
    i = 0
    j = 0
    k = s
    
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            
        else:
            arr[k] = right[j]
            j += 1
            
        k += 1
        
    while i < n1:
        arr[k] = left[i]
        i += 1
        k+= 1
        
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
 
    
def MergeSort(arr, s, e):
    
    if s < e:
        m = (s + e) // 2
        MergeSort(arr, s, m)
        MergeSort(arr, m+1, e)
        Merge(arr, s, m, e)
        
        
    return arr   
        

lst = [4,6,5,1,3,0]
sorted_lst = MergeSort(lst, 0, len(lst)-1)
print(sorted_lst)