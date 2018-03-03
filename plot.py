import sklearn.manifold
import json

from plotly.graph_objs import Scatter, Figure, Layout
from plotly.offline import plot

data = json.load(open('res.json'))
mat = list(data.values())

mds = sklearn.manifold.MDS()
fit = mds.fit_transform(mat)

trace = Scatter(
	x=fit[:,0],
	y=fit[:,1],
	mode='markers',
	text=list(data.keys()),
)

#layout = Layout(hovermode= 'closest')
#figure = Figure(data=trace)

plot([trace])