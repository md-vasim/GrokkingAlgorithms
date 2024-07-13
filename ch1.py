def binary_search(items, item):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low+high) 
        guess = items[mid]
        if guess == item:
            return item 
        if guess > item:
            high = mid - 1 
        else: 
            high = mid +1 
            
    return None 


items = [22,34,45,53,67,90,97]
print(binary_search(items, 53))