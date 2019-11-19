import plotly.graph_objects as go
import math

i = 0
X = []
Y = []
while i <= 10:
    X.append(i)
    Y.append(math.exp(-i))
    i += 0.1

fig = go.Figure(  
  data=[go.Scatter(x=X, y=Y)],
  layout_title_text="Graph"
  )
fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
fig.show()
