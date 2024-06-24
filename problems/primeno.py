#+++++++++++++++++++++++given 10 up to 10 what are the below prime no's++++++++++++++++++++++++++++
# def is_prime_basic(n):
 
#     for i in range(2, n+1):
#         if n % i == 0:
#             break
#         else:
#          print('prime',n)
#          break
# for n in range(2,10):    
#  is_prime_basic(n)
#+++++++++++++++++++++++++++Given no is prime are not++++++++++++++++++++++++++++++++++++++++++++++++++
# def is_prime_basic(n):
 
#     for i in range(2, n+1):
#         if n % i == 0:
#             break
#         else:
#          print('prime',n)
#          break    
# is_prime_basic(10)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
def is_prime_basic(m):
  for n in range(1,m):
    if n <= 1:
        print('False')
    for i in range(2, n):
        if n % i == 0:
            print(n,'is not a prime')
            break
        else:
          print(n,'is a prime number')
          break
               
is_prime_basic(10)