import requests, re, json
from registry import categories, municipalities

def get_num(mun_no, cat_no):
	params = {'cat_no': cat_no, 'mun_no': mun_no}
	url = 'https://www.blocket.se/hela_sverige?cg={cat_no}&w=0&st=s&ps=&ca={mun_no}'.format(**params)
	res = requests.get(url)
	html = res.text
	m = re.search(r'"num_hits">(.*?)<', html)
	return int(m.group(1))

def get_vector(mun_no):
	vec = []
	for cat_no in categories:
		num = get_num(mun_no, cat_no)
		vec.append(num)
	return [x/sum(vec) for x in vec]

def main():
	res = {}
	
	for mun_no, mun_name in municipalities.items():
		print(mun_name)
		vec = get_vector(mun_no)
		res[mun_name] = vec
		print('{}\n'.format([round(x,2) for x in vec]))

	out = json.dumps(res, sort_keys=True, indent=4)
	print(out)

if __name__ == '__main__':
	main()