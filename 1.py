# #  revursive 
# def fib_recursive(n):
#     if n <= 1:
#         return n
#     return fib_recursive(n-1) + fib_recursive(n-2)


# # ---- USER INPUT ----
# n = int(input("Enter n: "))

# print("Fibonacci number is:", fib_recursive(n))



# iterative
def fib_iterative(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


# ---- USER INPUT ----
n = int(input("Enter n: "))

print("Fibonacci number is:", fib_iterative(n))
