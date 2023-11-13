import random as rand

def w(L, i):
  return 1*i/(2*L-1)

def L(i, j):
  return (1/2*(i**2+j**2)**(1/2))+1/2

def evaluate_w(L, i, j):
  return[w(L, i), w(L, j)]


def get_magitude(vector):
  return (vector[0]**2 + vector[1]**2)**(1/2)

def verify(i, j):
  lambda_symbol = L(i, j)
  x=evaluate_w(lambda_symbol, i, j)
  return get_magitude(x)


for i in range(100000):
  # generate random int number between 1 and 1000
  i = rand.randint(1, 1000)
  j = rand.randint(1, 1000)
  if verify(i, j) > 1.0001 or verify(i, j) < 0.9999: # account for floating point error
    print("i: ", i, "j: ", j, "L: ", L(i, j), "w: ", evaluate_w(L(i, j), i, j), "mag: ", verify(i, j))
    break

