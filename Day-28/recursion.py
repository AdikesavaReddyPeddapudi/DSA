'''

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input("Enter a number: "))
print(f'Factorial of {n} is : {fact(n)}')

# direct recursion
def print_no(n):
  if n==0:
    return
  print(n)
n=7
print_no(n-1)
# indirect recursion
def even(n):
   if n==0:
      return True
   return odd(n-1)

def odd(n):
   if n==1:
      return False
   return even(n-1)
n=7
print(odd(n))


# Head Recursion
def print_no(n):
    if n==0:
        return 
    print_no(n-1)
    print(n)
n=5
print(print_no(n))
'''
# Tree Recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
n=7
print(fib(n))