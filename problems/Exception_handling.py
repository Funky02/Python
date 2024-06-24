
class CustomError(Exception):
    pass

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Please enter numbers only.")
    else:
        return result
    finally:
        print("Execution of divide_numbers complete.")

def main():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        if a < 0 or b < 0:
            raise CustomError("Negative numbers are not allowed.")
        result = divide_numbers(a, b)
        if result is not None:
            print(f"Result: {result}")
    except CustomError as e:
        print(e)
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()




########################EXCEPTION########################

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Please enter a valid number.")
# else:
#     print(f"The result is {result}")

#+++++++++++++++++++++++++Final block++++++++++++++++++++++++++++++++++++++

# try:
#     f = open('example.txt', 'r')
#     content = f.read()
# except FileNotFoundError:
#     print("Error: The file was not found.")
# finally:
#     f.close()
#     print("File closed.")

#++++++++++++++++++++++Raise Exception+++++++++++++++++++++++++++++++++++++++++++

# try:
#     age = int(input("Enter your age: "))
#     if age < 18:
#         raise ValueError("You must be at least 18 years old.")
# except ValueError as e:
#     print(e)
# else:
#     print("Access granted.")
    
    
#++++++++++++++++++++++++++CUSTOM Exception+++++++++++++++++++++++++++++++++++

# class AgeTooSmallError(Exception):
#     pass

# try:
#     age = int(input("Enter your age: "))
#     if age < 18:
#         raise AgeTooSmallError("Age is too small.")
# except AgeTooSmallError as e:
#     print(e)
# else:
#     print("Age is acceptable.")

####################################

# try:
#      a = int(input("Enter a number: "))
#      b = int(input("Enter another number: "))
#      result = a / b
# except Exception as e:
#      print("Error: Division by zero is not allowed.")