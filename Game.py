import random
import plotly
from plotly.graph_objs import Bar, Layout
from tabulate import tabulate

# Setup a class to make lots of Markets objects
# A class is an instruction to make an object
class Market:
  def __init__(self, wood, stone, coal, iron):
    self.wood = wood
    self.stone = stone
    self.coal = coal
    self.iron = iron

# Make object Market1 which requires 2 wood and 2 stone
Market1 = Market(2, 2, 0, 0)
# Makes 1 Komputer

# Make object Market2 which requires 1 coal and 1 iron
Market2 = Market(0, 0, 1, 1)
# Makes 1 Plane

# Set initial resources randomly (D6)
W = random.randint(1,6)
S = random.randint(1,6)
C = random.randint(1,6)
I = random.randint(1,6)
K = 0
P = 0
Z = 0

# Function which determines if there are sufficient commodities
# for Market1 to make a Komputer resource
def Market1_buy():
  global W, S, K
# Market 1 tries to turn commodities into resources until it can't
  while W >= 2 and S >= 2:
    #print("Market1 buys Komputer!")
    W = W - Market1.wood
    S = S - Market1.stone
    K = K + 1
  #else:
    #print("Not enough resources for Market 1!")

# Function which determines if there are sufficient commodities
# for Market2 to make a Plane resource
def Market2_buy():
  global C, I, P
# Market 1 tries to turn commodities into resources until it can't
  while C >= 1 and I >= 1:
    #print("Market2 buys Plane!")
    C = C - Market2.coal
    I = I - Market2.iron
    P = P + 1
  #else:
    #print("Not enough resources for Market 2!")



"""
#Open file
f = open("gamestate.txt","w+")
# Print starting commodities and resources
f.write("Wood " '{:01d}\n'.format(W))
f.write("Stone " '{:01d}\n'.format(S))
f.write("Coal " '{:01d}\n'.format(C))
f.write("Iron " '{:01d}\n'.format(I))
f.write("Komputer " '{:01d}\n'.format(K))
f.write("Plane " '{:01d}\n'.format(P))
f.write("Zoobium " '{:01d}\n'.format(Z))
f.close()
"""

# Ask for number of iterations
print("How many iterations?")
iterations = int(input())

i = 1
while i <= iterations:
  print("Iteration", i)
  # Markets buy what they can
  Market1_buy()
  Market2_buy()
  # Repopulate commodities by D6
  W = W + random.randint(1,6)
  S = S + random.randint(1,6)
  C = C + random.randint(1,6)
  I = I + random.randint(1,6)
  i += 1
  table = [["Wood",W],["Stone",S],["Coal",C],["Iron",I],["Komputer",K],
           ["Plane",P],["Zoobium",Z]]
  print(tabulate(table, headers=["Resources","Amount"]))
  print("")

"""
# Print finishing commodities and resources
#Open file
f = open("gamestate.txt","a")
# Print starting commodities and resources
f.write("Wood2 " '{:01d}\n'.format(W))
f.write("Stone2 " '{:01d}\n'.format(S))
f.write("Coal2 " '{:01d}\n'.format(C))
f.write("Iron2 " '{:01d}\n'.format(I))
f.write("Komputer2 " '{:01d}\n'.format(K))
f.write("Plane2 " '{:01d}\n'.format(P))
f.write("Zoobium2 " '{:01d}\n'.format(Z))
f.close()
"""
