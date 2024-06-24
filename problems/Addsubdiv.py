def calculator(n1,n2,opr): # function parameters are local variables
    def add():
        return n1+n2
    def sub():
        return n1-n2
    def multiply():
        return n1*n2
    def div():
        return n1/n2
    
    
    if opr=='+':
       return add()
    elif opr=='-':
        return sub()
    elif opr=='*':
        return multiply()
    elif opr=='/':
        return div()
    
    

def main():
    num1=int(input("Enter first number "))
    num2=int(input("Enter second number "))
    opr=input("Enter Operator ")
    result=calculator(num1,num2,opr)
    print(f'result of {num1}{opr}{num2}={result}')


main()
