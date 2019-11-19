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

"""
Adjust these lines of code to make any number of factories/markets
Factories make Resources
Markets make VP
This could be automated in the future
Idea: market changes based on game state
Idea: Dynamically generate markets
"""

def factory1():
  global W,S,C,I,K,P,Z,VP
  # Make factory which requires 2 Wood and 2 Stone
  # Makes 1 Komputer
  market = [2, 2, 0, 0, 1, 0, 0, 0]
  # factory1 tries to turn commodities into resources until it can't
  while True:
    # Check there are enough commodities to buy:
    rules = [W >= market[0],
             S >= market[1],
             C >= market[2],
             I >= market[3]]
    if all(rules):
      print("f1:Buy")
      W = W - market[0]
      S = S - market[1]
      C = C - market[2]
      I = I - market[3]
      K = K + market[4]
      P = P + market[5]
      Z = Z + market[6]
      VP = VP + market[7]     
    else:
      print("f1:Stop buying")
      print("")
      break

def factory2():
  global W,S,C,I,K,P,Z,VP
  # Make factory which requires 1 coal and 1 iron
  # Makes 2 Planes
  market = [0, 0, 1, 1, 0, 2, 0, 0]
  # factory2 tries to turn commodities into resources until it can't
  while True:
    # Check there are enough commodities to buy:
    rules = [W >= market[0],
             S >= market[1],
             C >= market[2],
             I >= market[3]]
    if all(rules):
      print("f2:Buy")
      W = W - market[0]
      S = S - market[1]
      C = C - market[2]
      I = I - market[3]
      K = K + market[4]
      P = P + market[5]
      Z = Z + market[6]
      VP = VP + market[7]     
    else:
      print("f2:Stop buying")
      print("")
      break

def market1():
  global W,S,C,I,K,P,Z,VP
  # Make market which requires 3 Komputer and 5 Plane
  # Makes 1 VP
  market = [0, 0, 0, 0, 3, 4, 0, 1]
  # market1 tries to turn commodities into resources until it can't
  while True:
    # Check there are enough commodities to buy:
    rules = [K >= market[4],
             P >= market[5],
             Z >= market[6]]
    if all(rules):
      print("m1:Buy")
      W = W - market[0]
      S = S - market[1]
      C = C - market[2]
      I = I - market[3]
      K = K - market[4]
      P = P - market[5]
      Z = Z - market[6]
      VP = VP + market[7]     
    else:
      print("m1:Stop buying")
      print("")
      break

def market2():
  global W,S,C,I,K,P,Z,VP
  # Make market which requires random resources to make VP
  # Makes 1 VP
  market = [0, 0, 0, 0, 0, 0, 0, 1]
  market[0] = random.randint(0,2)
  market[1] = random.randint(0,2)
  market[2] = random.randint(0,2)
  market[3] = random.randint(0,2)
  market[4] = random.randint(0,2)
  market[5] = random.randint(0,2)
  # market1 tries to turn commodities into resources until it can't
  while True:
    # Check there are enough commodities to buy:
    rules = [W >= market[0],
             S >= market[1],
             C >= market[2],
             I >= market[3],
             K >= market[4],
             P >= market[5],
             Z >= market[6]]
    if all(rules):
      print("m2:Buy")
      W = W - market[0]
      S = S - market[1]
      C = C - market[2]
      I = I - market[3]
      K = K - market[4]
      P = P - market[5]
      Z = Z - market[6]
      VP = VP + market[7]     
    else:
      print("m2:Stop buying")
      print("")
      break
  
"""
End of market generation
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
  # factories/markets buy what they can
  factory1()
  factory2()
  market1()
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



