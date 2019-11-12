import plotly.graph_objects as go
import numpy as np
#from plotly.graph_objs import Bar, Layout

resources = []
values = []

#Open data file
f = open("gamestate.txt","r")
for line in f:
    a,b = line.strip().split()
    resources.append(a)
    b = int(b)
    values.append(b)
f.close()

print(resources)
print(values)

fig = go.Figure(
    data=[go.Bar(x=resources, y=values)],
    layout_title_text="XXXXX"
)
fig.show()
