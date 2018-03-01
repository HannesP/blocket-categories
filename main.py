import requests, re
from registry import categories, municipalities

def get_num(mun_no, cat_no):
	params = {'cat_no': cat_no, 'mun_no': mun_no}
	url = 'https://www.blocket.se/hela_sverige?cg={cat_no}&w=0&st=s&ps=&ca={mun_no}'.format(**params)
	res = requests.get(url)
	html = res.text
	m = re.search(r'"num_hits">(.*?)<', html)
	return m.group(1)

def main():
	for mun_no, mun_name in municipalities.items():
		print(mun_name)
		print('=' * len(mun_name))
		
		for cat_no, cat_name in categories.items():
			num = get_num(mun_no, cat_no)
			print('{}: {}'.format(cat_name, num))
		print()

if __name__ == '__main__':
	main()