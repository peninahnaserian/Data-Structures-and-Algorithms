def selectionsort(arr):
    for i in range(len(arr)):
        min_ind = i
        
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        #swapping the elements to sort the array
        #if (ind != min_index):
        (arr[i],arr[min_ind]) = (arr[min_ind],arr[i])
    return arr
        
arr = [5,2,3,1]


selectionsort(arr)
print("The array after sorting in ascending order by selection sort is:",arr)