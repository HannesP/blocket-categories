import json
from collections import defaultdict

import sklearn.manifold
from plotly.graph_objs import Scatter, Figure, Layout
from plotly.offline import plot

from registry import municipalities

regions = [
	'Skåne',
	'Norrbotten',
	'Västerbotten',
	'Jämtland',
	'Västernorrland',
	'Gävleborg',
	'Dalarna',
	'Värmland',
	'Örebro',
	'Västmanland',
	'Uppsala',
	'Stockholm',
	'Södermanland',
	'Skaraborg',
	'Östergötland',
	'Göteborg',
	'Älvsborg',
	'Jönköping',
	'Kalmar',
	'Gotland',
	'Halland',
	'Kronoberg',
	'Blekinge'
]

def mun_name_to_reg_no(mun_name):
	info = municipalities[mun_name]
	if len(info) == 2:
		return int(info[1])
	elif '23_' in info[0]:
		return 0
	else:
		return 1

def indices_for_reg_no(reg_no, munis):
	return [i for i, mun_name in enumerate(munis) if mun_name_to_reg_no(mun_name) == reg_no]

data = json.load(open('res.json'))
mat = list(data.values())

mds = sklearn.manifold.MDS()
fit = mds.fit_transform(mat)

traces = []
for reg_no in range(23):
	try:
		indices = indices_for_reg_no(reg_no, data.keys())
		trace = Scatter(
			x=fit[indices,0],
			y=fit[indices,1],
			mode='markers',
			text=[list(data.keys())[i] for i in indices],
			name=regions[reg_no]
		)
		traces.append(trace)
	except:
		raise
	
layout = Layout(
	hovermode='closest'
)

figure = Figure(data=traces, layout=layout)
plot(figure)