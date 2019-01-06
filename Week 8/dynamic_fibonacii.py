# Dynamic fibonacci 
def fib(n):
    fibtable[0] = 0
    fibtable[1] = 1
    for i in range(2, n+1):
        fibtable[i] = fibtable[i-1] + fibtable[i-2]
        print(i)
    print(list(fibtable))

if __name__ == 'main':
    print(fib(100))
