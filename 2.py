# bst

# recursive 

def binary_search_recursive(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search_recursive(arr, low, mid - 1, key)
    else:
        return binary_search_recursive(arr, mid + 1, high, key)


# ---- USER INPUT ----
n = int(input("Enter number of books: "))
arr = list(map(int, input("Enter sorted ISBN list: ").split()))
key = int(input("Enter ISBN to search: "))

result = binary_search_recursive(arr, 0, n - 1, key)
print("Recursive Search Output:", result)

# iterative

def binary_search_iterative(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    return -1


# ---- USER INPUT ----
n = int(input("Enter number of books: "))
arr = list(map(int, input("Enter sorted ISBN list: ").split()))
key = int(input("Enter ISBN to search: "))

print("Iterative Search Output:", binary_search_iterative(arr, key))

