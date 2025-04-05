
def rec_fibo(n):
    if n <= 1:
        return n
    else:
        return(rec_fibo(n-1) + rec_fibo(n-2))
    
n = 5
print("Fibonacci sequence:")
for i in range(n):
    print(rec_fibo(i))
