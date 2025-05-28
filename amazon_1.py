def minimalHeaviestSetA(arr):
    subset_size = 1
    
    for i in range(1, len(arr)):
        sorted_array = sorted(arr) # return a new list

        