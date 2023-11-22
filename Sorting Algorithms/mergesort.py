def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        
        #dividing array into two halves
        left_array = arr[:mid]
        right_array = arr[mid:]
        
        #calling mergesortfunction on subparts of array using recursion
        merge_sort(left_array)
        merge_sort(right_array)
        
        i = j = k = 0
        
        #copying data to temp arrays left_array[] and right_array[]
        
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1
        #checking if any element was left
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1
    return arr
            
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
            
    
arr = [6,5,12,10,9,1]
                
merge_sort(arr)

print_list(arr)

#print(3//2) #1