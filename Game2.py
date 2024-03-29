import random
import plotly
import numpy as np
import plotly.graph_objects as go
from tabulate import tabulate

dict_resources = {
  "Wa":"Wood",
  "Sa":"Stone",
  "Ca":"Coal",
  "Ia":"Iron",
  "Ka":"Komputers",
  "Pa":"Planes",
  "Za":"Zoobium",
  "VPa":"Victory Points"
  }

# Setup a class to make lots of factory objects
# A class is an instruction to make an object
class factory:
  def __init__(self, wood, stone, coal, iron, komputer, plane, zoobium, vp):
    self.wood = wood
    self.stone = stone
    self.coal = coal
    self.iron = iron
    self.komputer = komputer
    self.plane = plane
    self.zoobium = zoobium
    self.vp = vp

# Make object factory1 which requires 2 wood and 2 stone
factory1 = factory(2, 2, 0, 0, 0, 0, 0, 0)
# Makes 1 Komputer

# Make object factory2 which requires 1 coal and 1 iron
factory2 = factory(0, 0, 1, 1, 0, 0, 0, 0)
# Makes 1 Plane

# Make object factory3 which turns komputers and planes into VP
factory3 = factory(0, 0, 0, 0, 3, 7, 0, 0)

# Set initial resources randomly (D6)
W = random.randint(1,6)
S = random.randint(1,6)
C = random.randint(1,6)
I = random.randint(1,6)
K = 0
P = 0
Z = 0
VP = 0

# Function which determines if there are sufficient commodities
# for factory1 to make a Komputer resource
def factory1_buy():
  global W, S, K
# factory 1 tries to turn commodities into resources until it can't
  while W >= factory1.wood and S >= factory1.stone:
    W = W - factory1.wood
    S = S - factory1.stone
    K = K + 1

# Function which determines if there are sufficient commodities
# for factory2 to make a Plane resource
def factory2_buy():
  global C, I, P
# factory 1 tries to turn commodities into resources until it can't
  while C >= factory2.coal and I >= factory2.iron:
    C = C - factory2.coal
    I = I - factory2.iron
    P = P + 1

# Function which determines if there are sufficient commodities
# for factory3 to make a VP
def factory3_buy():
  global K, P, VP
# factory 1 tries to turn commodities into resources until it can't
  while K >= factory3.komputer and P >= factory3.plane:
    K = K - factory3.komputer
    P = P - factory3.plane
    VP = VP + 1

Wa,Sa,Ca,Ia,Ka,Pa,Za,VPa = [W],[S],[C],[I],[K],[P],[Z],[VP]




# Ask for number of iterations
print("How many iterations?")
iterations = int(input())

i = 1
X = [i]
while i <= iterations:
  print("Iteration", i)
  # factories buy what they can
  factory1_buy()
  factory2_buy()
  factory3_buy()
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
  X.append(i)
  print("")

print(X)
print(VPa)

fig = go.Figure(  
  data=[go.Scatter(x=X, y=VPa)],
  layout_title_text=dict_resources["VPa"]
  )
fig.show()


