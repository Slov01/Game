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

# Setup a class to make lots of market objects
# A class is an instruction to make an object
# Markets turn commodities and resources into anything
class market:
  def __init__(self, wood, stone, coal, iron, \
               komputer, plane, zoobium, victory):
    self.wood = wood
    self.stone = stone
    self.coal = coal
    self.iron = iron
    self.komputer = komputer
    self.plane = plane
    self.zoobium = zoobium
    self.victory = victory

"""
Adjust these lines of code to make any number of market objects
This could be automated in the future
"""



# Make object market1 which requires 2 wood and 2 stone
market1 = market(2, 2, 0, 0, 7, 0, 0, 0)
# Makes 1 Komputer
# Function to convert between resources and commodities
def market1_buy():
  global W,S,C,I,K,P,Z,VP
# market1 tries to turn commodities into resources until it can't
  rules = [W >= market1.wood,
           S >= market1.stone,
           C >= market1.coal,
           I >= market1.iron]
  while True:
    #if all(rules):
    if W >= market1.wood:
      print(W,S,C,I,K,P,Z,VP)
      W = W - market1.wood
      S = S - market1.stone
      C = C - market1.coal
      I = I - market1.iron
      K = K + market1.komputer
      P = P + market1.plane
      Z = Z + market1.zoobium
      VP = VP + market1.victory
      print(" Buy again")
      print("")
    else:
      print(W,S,C,I,K,P,Z,VP)
      print("Break")
      break




# Make object market2 which requires 1 coal and 1 iron
market2 = market(0, 0, 1, 1, 0, 1, 0, 0)
# Makes 1 Plane

# Make object market3 which requires 3 komputers and 7 planes
market3 = market(0, 0, 0, 0, 3, 7, 0, 1)
# Makes 1 VP

"""
End of object generation
"""




# Function which determines if there are sufficient commodities
# for market2 to make a Plane resource
def market2_buy():
  global C, I, P
# market2 tries to turn commodities into resources until it can't
  while C >= market2.coal and I >= market2.iron:
    C = C - market2.coal
    I = I - market2.iron
    P = P + 1

# Function which determines if there are sufficient commodities
# for market3 to make a VP
def market3_buy():
  global K, P, VP
# market3 tries to turn resources into VP until it can't
  while K >= market1.komputer and P >= market1.plane:
    K = K - market1.komputer
    P = P - market1.plane
    VP = VP + 1

# These arrays are used to store the historical resource amounts
Wa,Sa,Ca,Ia,Ka,Pa,Za,VPa = [W],[S],[C],[I],[K],[P],[Z],[VP]





# Ask for number of iterations
print("How many iterations?")
iterations = int(input())

# Print starting resources table
print ("Starting resources")
table = [["Wood",W],["Stone",S],["Coal",C],["Iron",I],["Komputer",K],
           ["Plane",P],["Zoobium",Z],["Victory points",VP]]
print(tabulate(table, headers=["Resources","Amount"]))
print("")
# Start iterations
i = 1
X = [0]
while i <= iterations:
  print("Iteration", i)
  X.append(i)
  # markets buy what they can
  market1_buy()
  #market2_buy()
  #market3_buy()
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



