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

# Set initial commodities randomly (D6)
W = random.randint(1,6)
S = random.randint(1,6)
C = random.randint(1,6)
I = random.randint(1,6)
# Set initial resources and VP to 0
K = 0
P = 0
Z = 0
VP = 0

# This array stores the current level of resources
resource_bank = [W,S,C,I,K,P,Z,VP]

# These arrays are used to store the historical resource amounts
Wa,Sa,Ca,Ia,Ka,Pa,Za,VPa = [W],[S],[C],[I],[K],[P],[Z],[VP]

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
Idea: market changes based on game state
"""

# Make object market1 which requires 2 wood and 2 stone
market1 = market(2, 2, 0, 0, 1, 0, 0, 0)
# Makes 1 Komputer
# Function to convert between resources and commodities
def market1_buy():
  global W,S,C,I,K,P,Z,VP
# market1 tries to turn commodities into resources until it can't
  while True:
    # Check there are enough commodities to buy:
    rules = [W >= market1.wood,
             S >= market1.stone,
             C >= market1.coal,
             I >= market1.iron]
    if all(rules):
      print("1:Buy")
      W = W - market1.wood
      S = S - market1.stone
      C = C - market1.coal
      I = I - market1.iron
      K = K + market1.komputer
      P = P + market1.plane
      Z = Z + market1.zoobium
      VP = VP + market1.victory      
    else:
      print("1:Stop buying")
      print("")
      break

# Make object market2 which requires 1 coal and 1 iron
market2 = market(0, 0, 1, 1, 0, 2, 0, 0)
# Makes 2 Planes
# Function to convert between resources and commodities
def market2_buy():
  global W,S,C,I,K,P,Z,VP
# market2 tries to turn commodities into resources until it can't
  while True:
    # Check there are enough commodities to buy:
    rules = [W >= market2.wood,
             S >= market2.stone,
             C >= market2.coal,
             I >= market2.iron]
    if all(rules):
      print("2:Buy")
      W = W - market2.wood
      S = S - market2.stone
      C = C - market2.coal
      I = I - market2.iron
      K = K + market2.komputer
      P = P + market2.plane
      Z = Z + market2.zoobium
      VP = VP + market2.victory      
    else:
      print("2:Stop buying")
      print("")
      break

# Make object market3 which requires 3 komputers and 7 planes
market3 = market(0, 0, 0, 0, 3, 7, 0, 1)
# Makes 1 VP
# Function to convert between resources and commodities
def market3_buy():
  global W,S,C,I,K,P,Z,VP
# market3 tries to turn commodities into resources until it can't
  while True:
    # Check there are enough commodities to buy:
    rules = [K >= market3.komputer,
             P >= market3.plane,
             Z >= market3.zoobium,
             VP < 10]
    if all(rules):
      print("3:Buy")
      W = W + market3.wood
      S = S + market3.stone
      C = C + market3.coal
      I = I + market3.iron
      K = K - market3.komputer
      P = P - market3.plane
      Z = Z - market3.zoobium
      VP = VP + market3.victory      
    else:
      print("3:Stop buying")
      print("")
      break

"""
End of object generation
"""


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
  market2_buy()
  market3_buy()
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

plot0 = go.Scatter(x=X, y=mega_array[0], name = tuple_resources[0])
plot1 = go.Scatter(x=X, y=mega_array[1], name = tuple_resources[1])
plot2 = go.Scatter(x=X, y=mega_array[2], name = tuple_resources[2])
plot3 = go.Scatter(x=X, y=mega_array[3], name = tuple_resources[3])
plot4 = go.Scatter(x=X, y=mega_array[4], name = tuple_resources[4])
plot5 = go.Scatter(x=X, y=mega_array[5], name = tuple_resources[5])
plot6 = go.Scatter(x=X, y=mega_array[6], name = tuple_resources[6])
plot7 = go.Scatter(x=X, y=mega_array[7], name = tuple_resources[7])

fig1 = go.Figure(  
  data=[plot0, plot1, plot2, plot3],
  layout_title_text="Commodities"
  )
fig1.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
fig1.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
fig1.show()

fig2 = go.Figure(  
  data=[plot4, plot5, plot6, plot7],
  layout_title_text="Resources and Victory Points"
  )
fig2.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
fig2.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
fig2.show()



