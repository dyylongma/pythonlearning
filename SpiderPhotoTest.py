import urllib.request
import os
from bs4 import BeautifulSoup

# open url
url = 'https://pixabay.com/zh/photos/?q=%E5%A4%B4%E5%83%8F&hp=&image_type=all&order=&cat=&min_width=&min_height='
res = urllib.request.urlopen(url)
html = res.read()
soup = BeautifulSoup(html,'html.parser')

#find img lab
result = soup.find_all('img')
links = []
index = 0

#find N pieces
for content in result:
	if index < 10:
		s = content.get('srcset')
		if s is None:
			ss = s
		else:
			links.append(s.split(' ')[0])
	index += 1

print (len(links))

#mkdir
if not os.path.exists('photo'):
	os.makedirs('photo')

i = 0
for link in links:
	i+=1
	filename = 'photo\\' + 'photo' + str(i) + '.jpg'
	with open(filename,'w'):
		urllib.request.urlretrieve(link,filename)