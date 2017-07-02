import requests 
from bs4 import BeautifulSoup
'''
# example code
source_code = requests.get("https://en.wikipedia.org/wiki/Sustainable_energy").text
soup = BeautifulSoup(source_code)
b = soup.find_all("a")
'''
# times = 0
def bfs(total, url_set):
	result = []
	for url in url_set:
		source_code = requests.get(url).text
		soup = BeautifulSoup(source_code)
		for para in soup.find_all("p"):
			for item in para.find_all("a"):
				if item.get("href",0)!=0 and "/wiki/" in item['href'] and "#" not in item['href'] and ":"  not in item['href']:
					if "solar" in item.get("href").lower() or "solar" in item.text.lower():
						new_url = "https://en.wikipedia.org" + item['href']
						if new_url not in total:
							result.append(new_url)
							total.append(new_url)
	return result
current, total = ["https://en.wikipedia.org/wiki/Sustainable_energy"], ["https://en.wikipedia.org/wiki/Sustainable_energy"]
for _ in range(4):
	current = bfs(total, current)
for item in total:
	print item