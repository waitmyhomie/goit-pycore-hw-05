def caching_fibonacci():
    # create an emptz dictionarz for caching fibonacci results
    cache = {}

    # inner function to calculate fibonacci numbers
    def fibonacci(n):
        # base cases
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # if the number is in cache, return it
        if n in cache:
            return cache[n]

        # calculate fibonacci number recursively and store result in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # return the inner function
    return fibonacci


fib = caching_fibonacci()
print(fib(10))  # prints 55
print(fib(15))  # prints 610