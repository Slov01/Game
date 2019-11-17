import random
import plotly
import numpy as np
import plotly.graph_objects as go
from tabulate import tabulate

# Set a tuple of resource names.  Indexing starts from 0
tuple_resources = (
  "Wood",
  "Stone",
  "Coal",
  "Iron",
  "Komputers",
  "Planes",
  "Zoobium",
  "Victory Points"
  )

# Setup a class to make lots of factory objects
# A class is an instruction to make an object
class factory:
  def __init__(self, wood, stone, coal, iron):
    self.wood = wood
    self.stone = stone
    self.coal = coal
    self.iron = iron

# Setup a class to make lots of market objects
# A class is an instruction to make an object
class market:
  def __init__(self, komputer, plane, zoobium, vp):
    self.komputer = komputer
    self.plane = plane
    self.zoobium = zoobium
    self.vp = vp

# Make object factory1 which requires 2 wood and 2 stone
factory1 = factory(2, 2, 0, 0)
# Makes 1 Komputer

# Make object factory2 which requires 1 coal and 1 iron
factory2 = factory(0, 0, 1, 1)
# Makes 1 Plane

# Make object market1 which turns komputers and planes into VP
market1 = market(3, 7, 0, 0)

# Set initial resources randomly (D6)
W = random.randint(1,6)
S = random.randint(1,6)
C = random.randint(1,6)
I = random.randint(1,6)
K = 0
P = 0
Z = 0
VP = 0

resource_bank = [W,S,C,I,K,P,Z,VP]

# Function which determines if there are sufficient commodities
# for factory1 to make a Komputer resource
def factory1_buy():
  global W, S, K
# factory1 tries to turn commodities into resources until it can't
  while W >= factory1.wood and S >= factory1.stone:
    W = W - factory1.wood
    S = S - factory1.stone
    K = K + 1

# Function which determines if there are sufficient commodities
# for factory2 to make a Plane resource
def factory2_buy():
  global C, I, P
# factory2 tries to turn commodities into resources until it can't
  while C >= factory2.coal and I >= factory2.iron:
    C = C - factory2.coal
    I = I - factory2.iron
    P = P + 1

# Function which determines if there are sufficient commodities
# for market1 to make a VP
def market1_buy():
  global K, P, VP
# market1 tries to turn resources into VP until it can't
  while K >= market1.komputer and P >= market1.plane:
    K = K - market1.komputer
    P = P - market1.plane
    VP = VP + 1

# These arrays are used to store the historical resource amounts
Wa,Sa,Ca,Ia,Ka,Pa,Za,VPa = [W],[S],[C],[I],[K],[P],[Z],[VP]





# Ask for number of iterations
print("How many iterations?")
iterations = int(input())

i = 1
X = [i]
while i <= iterations:
  print("Iteration", i)
  X.append(i)
  # factories buy what they can
  factory1_buy()
  factory2_buy()
  # markets buy what they can
  market1_buy()
  table = [["Wood",W],["Stone",S],["Coal",C],["Iron",I],["Komputer",K],
           ["Plane",P],["Zoobium",Z],["Victory points",VP]]
  print(tabulate(table, headers=["Resources","Amount"]))
  Wa.append(W)
  Sa.append(S)
  Ca.append(C)
  Ia.append(I)
  Ka.append(K)
  Pa.append(P)
  Za.append(Z)
  VPa.append(VP)
  # Repopulate commodities by D6
  W = W + random.randint(1,6)
  S = S + random.randint(1,6)
  C = C + random.randint(1,6)
  I = I + random.randint(1,6)
  i += 1
  print("")

# Put all historical resources in a matrix
# Indexing starts from 0
# Array of all of the Wood would be mega_array[0]
mega_array = [Wa,Sa,Ca,Ia,Ka,Pa,Za,VPa]

print("Display which graph?")
print("Wood:0, Stone:1, Coal:2, Iron:3")
print("Komputers:4, Planes:5, Zoobium:6, Victory Points:7")
graph_name = int(input())
print("Resource choice=", tuple_resources[graph_name])
print("X =", X)
print("Y= ", mega_array[graph_name])

fig = go.Figure(  
  data=[go.Scatter(x=X, y=mega_array[graph_name])],
  layout_title_text=tuple_resources[graph_name]
  )
fig.show()



