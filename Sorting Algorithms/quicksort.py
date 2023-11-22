def partition(start,end,array):
    #initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]
    
    #this loop runs till tart pointer crosses
    #end pointer, and when it does we swap the
    #pivot with element on end pointer
    while start < end:
        #increment the start pointer till it finds an
        #element greater than pivot
        while start < len(array) and array[start] <= pivot:
            start += 1
            
            #decrement the end pointer till it finds an
            #element less than pivot
            while array[end] > pivot:
                end -= 1
                
            #if start and end have not crossed each other
            #swap the numbers on start and end
            if(start < end):
                array[start],array[end] = array[end],array[start]
                
    #swap pivot element with element on end pointer
    #this puts pivot on its correct sorted place
    array[end],array[pivot_index] = array[pivot_index], array[end]
    
    #returning end pointer to divide the array into 2
    return end

def quick_sort(start,end,array):
    if(start < end):
        #p is partitioning index, array[p]
        #is at right place
        p = partition(start, end, array)
        
        #sort elements before partition
        #and after partition
        quick_sort(start, p-1, array)
        quick_sort(p+1, end, array)
        
array = [10,7,8,9,1,5]
quick_sort(0,len(array)-1,array)

print("Sorted array is:",array)

            