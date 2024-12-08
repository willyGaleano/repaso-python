"""
#CASO 1
x = "asombroso"

def my_func():
  print("Python es " + x)

my_func()

#CASO 2
palabra = "awesome"

def my_func_2():
  palabra = "fantastic"
  print("Python is " + palabra)

my_func_2()

print("Python is " + palabra)


#CASO 3
def my_func_3():
  global y
  y = "fantastic"

my_func_3()

print("Python is " + y)

"""
#CASO 4

a = "awesome"

def my_func_4():
  global a
  a = "fantastic"

my_func_4()
print("Python is " + a)
