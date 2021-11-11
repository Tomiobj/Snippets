def fibonacci (num):
    i=2
    fib = [0,1]
    while i<num:
        fib.append(fib[-1]+fib[-2])
        i=i+1
        print(fib)
    return fib
    
fibonacci(8)
