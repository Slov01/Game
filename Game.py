import random
import plotly
from plotly.graph_objs import Bar, Layout

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

# Function which determines if there are sufficient commodities for Market1 to make a resource
def Market1_buy(x,y):
    print("Market1 buys Komputer!")
    global W, S, K
    W = W - Market1.wood
    S = S - Market1.stone
    K = K + 1

# Function which determines if there are sufficient commodities for Market2 to make a resource
def Market2_buy(x,y):
    print("Market2 buys Plane!")
    global C, I, P
    C = C - Market2.coal
    I = I - Market2.iron
    P = P + 1






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

# Market 1 tries to turn commodities into resources until it can't
while W >= 2 and S >= 2:
  Market1_buy(W,S)
else:
  print("Not enough resources for Market 1!")

# Market 2 tries to turn commodities into resources until it can't
while C >= 1 and I >= 1:
  Market2_buy(C,I)
else:
  print("Not enough resources for Market 2!")

# Print finishing commodities and resources
#Open file
f = open("gamestate.txt","a")
# Print starting commodities and resources
f.write("Wood " '{:01d}\n'.format(W))
f.write("Stone " '{:01d}\n'.format(S))
f.write("Coal " '{:01d}\n'.format(C))
f.write("Iron " '{:01d}\n'.format(I))
f.write("Komputer " '{:01d}\n'.format(K))
f.write("Plane " '{:01d}\n'.format(P))
f.write("Zoobium " '{:01d}\n'.format(Z))
f.close()

