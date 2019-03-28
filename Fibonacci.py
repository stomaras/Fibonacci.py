def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for f in fib():
    if f > 50:# I want to see Fibonacci numbers between 0 and 50 
        break
    print(f)
         
#terminated when it the village is number exceeded 50 because 31 and 34 and 21
#is 55
