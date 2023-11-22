def fibonacci_series(n):
    fib_series = [0, 1]

    for i in range(2, n):
        next_term = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_term)

    return fib_series

# Example: print Fibonacci series up to the 10th term
n = 10
result = fibonacci_series(n)
print("Fibonacci Series up to {} terms: {}".format(n, result))
