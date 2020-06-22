import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

x = -2.12e-18
y = sigmoid(x)
print(y)
x = 2.12e-18
y = sigmoid(x)
print(y)
x= 4.24e-18
y= 8.75e-27
z= -0.5*x -1*y
print(z)
z= 0.5*x+1*y
print(z)
a= math.exp(0.5)
b= math.exp(0.5)
c = a+b
print(a/c)
print(b/c)
a= 0.03125
z= a*x
print(z)
z= a*y
print(z)
z= -0.03125 * x * (1-x)
print(z)
z= -0.0625 * y *(1-y)
print(z)
f = -1.325e-19
u = -5.468e-28
print(u*40)
print(u*80)