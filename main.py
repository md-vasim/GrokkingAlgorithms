def find_smallest(arr):
    smallest = arr[0]
    smallest_idx = 0 
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i 
    return smallest_idx

def selection_sort(arr):
    new_list = [] 
    for i in range(len(arr)):
        smallest_idx = find_smallest(arr)
        new_list.append(arr.pop(smallest_idx)) 

    return new_list

arr = [33,23,98,67,45,54,10]



print(arr)
print(selection_sort(arr))

