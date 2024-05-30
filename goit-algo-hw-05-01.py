def create_caching_function(func):
    cache = {}

    def caching_function(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return caching_function

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

caching_fibonacci = create_caching_function(fibonacci)

cached_fib = caching_fibonacci
print(cached_fib(10))
print(cached_fib(15))
