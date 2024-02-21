def fibonacci_dynamic(n):
    if n <= 1:
        return n
    
    #initialize a table to store intermediate results
    fib_table = [0] * (n+1)
    fib_table[1] = 1

    #build the fibonacci sequence bottom-up
    for i in range(2, n+1):
        fib_table[i] = fib_table[i-1] + fib_table[i-2]

    return fib_table[n]

#print example usage

print(fibonacci_dynamic(5))
print(fibonacci_dynamic(8))