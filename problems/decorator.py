def decorator1(f): # Outer function
    def fun2(): # Inner function
        f()
        print("transformed function")
    return fun2

@decorator1
def fun1():
    print("This is function1")

# Interanal concept
#f2=decorator1(fun1)
#f2()
fun1()

