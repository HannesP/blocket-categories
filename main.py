import requests, re, json
from registry import categories, municipalities

def get_num(mun, cat_no):
	if len(mun) == 1:
		mun_no = mun[0]
		params = {'cat_no': cat_no, 'mun_no': mun_no}
		url_temp = 'https://www.blocket.se/hela_sverige?cg={cat_no}&ca={mun_no}&f=p'
	else:
		mun_no1, mun_no2 = mun
		params = {'mun_no1': mun_no1, 'mun_no2': mun_no2, 'cat_no': cat_no}
		url_temp = 'https://www.blocket.se/hela_sverige?q=&cg={cat_no}&w=1&m={mun_no1}&st=s&cs=&ck=&csz=&f=p&ca={mun_no2}&is=1&l=0&md=th'
		
	url = url_temp.format(**params)
	res = requests.get(url)
	html = res.text
	m = re.search(r'"num_hits">(.*?)<', html)
	return int(m.group(1))

def get_vector(mun):
	vec = []
	for cat_no in categories:
		num = get_num(mun, cat_no)
		vec.append(num)
	return [x/sum(vec) for x in vec]

def main():
	res = {}
	
	for mun_name, mun in municipalities.items():
		print(mun_name)
		vec = get_vector(mun)
		res[mun_name] = vec
		print('{}\n'.format([round(x,2) for x in vec]))

	out = json.dumps(res, sort_keys=True, indent=4)
	print(out)

if __name__ == '__main__':
	main()