import random

#Int

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#Float

a = 1.10
b = 1.0
c = -35.5948989855689

print(type(a))
print(type(b))
print(type(c))

#Complex
d = 3+5j
e = 5j
f = -5j

print(type(d))
print(type(e))
print(type(f))

#Conversión
num1 = 10    # int
num2 = 2.8  # float
num3 = 1j   # complex (0 + ij)

#convertir de int a float
resultado1 = float(num1)
print(resultado1)

#convertir de float a int
resultado2 = int(num2)
print(resultado2)


#convertir de int a complex
resultado3 = complex(num1)
print(resultado3)

print(random.randrange(1, 11))