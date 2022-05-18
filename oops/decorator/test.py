import time

def timeit(func):
    def timed(*args, **kwargs):
        start_time = time.time()
        print("Start time\t", start_time)
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        print("End time\t", end_time)
        
        total_time = ( end_time - start_time ) * 10 ** 6
        print("Total time\t %8.2f" % total_time)
        
        return result
    return timed

@timeit
def fib():
    a = 0
    b = 1
    while True:
        yield a
        a,b=b,a+b

num = int(input("Enter limit: "))
fibonacci = fib()

for x in range(num):
    print (next(fibonacci))
