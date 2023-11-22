def bubble_sort(arr):
    n = len(arr)
    
    #optimize code, so if the array is already sorted,
    # it doesn't need to go through the entire process
    swapped = False
    
    #traverse through all array elements
    for i in range(n-1): #starts at 0
        # range(n) also work but outer loop will
        # repeat one more time than needed
        # last i elements are already in place
        for j in range(0,n-i-1): #start at 0, stop at n-i-1
            # traverse the array from 0 to n-i-1
            # swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            # if we haven't needed to make a single swap,
            # we can just exit the main loop
            return
        
arr = [64, 34, 25, 12, 22, 11, 90]

print("The input array is:",arr)

bubble_sort(arr)

print("The sorted array is:",arr)