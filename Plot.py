import plotly.graph_objects as go
#from plotly.graph_objs import Bar, Layout

variable = []

#Open data file
f = open("gamestate.txt","r")
for line in f:
    a,b = line.strip().split()
    variable.append(b)

f.close()

fig = go.Figure(
    data=[go.Bar(x = ['WoodS','StoneS','CoalS','IronS','KomputerS','PlaneS','ZoobiumS','WoodF','StoneF','CoalF','IronF','KomputerF','PlaneF','ZoobiumF'],
                 y=[variable])],
    layout_title_text="XXXXX"
)
fig.show()
