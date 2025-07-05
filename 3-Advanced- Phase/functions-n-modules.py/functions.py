'''
def greet(name):
  print(f"hello, {name}")

greet("Mr JazziQ")

def add(a, b):
  return a + b


result = add(10, 55)
print(result)
'''

def factorial(a):
  if a == 0:
    return 1
  else:
    return a*factorial(a-1)
  
def greet(name, greeting="hello"):
  print(f"(greeting), (name)")
  
greet("jazzi", "Good Moring")
  