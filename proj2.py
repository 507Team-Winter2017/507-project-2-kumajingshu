#proj2.py


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url="http://www.newyorktimes.com"
fhand=urllib.request.urlopen(url,context=ctx)
html=fhand.read()
soup=BeautifulSoup(html,'html.parser')
headlinelist=list()
for story_heading in soup.find_all(class_="story-heading"):
	#print (story_heading)
	if story_heading.a:
		headline=story_heading.a.text.replace('\n', " ").strip()
		headlinelist.append(headline)
	else:
		headline=story_heading.contents[0].strip()
		headlinelist.append(headline)
for headline in headlinelist[0:10]:
	print (headline)
		

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url="http://www.michigandaily.com"
fhand=urllib.request.urlopen(url,context=ctx)
html=fhand.read()
soup=BeautifulSoup(html,'html.parser')
for headline in soup.find_all(class_="view-most-read"):
	print (headline.text)
#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url="http://newmantaylor.com/gallery.html"
fhand=urllib.request.urlopen(url,context=ctx)
html=fhand.read()
soup=BeautifulSoup(html,'html.parser')
for image in soup.find_all('img'):
	try:
		imagealt=image.get('alt')
		if imagealt==None:
			print('No alternative text provided!')
		else: 
			print(image.get('alt'))
	except:
		continue
#for img in imagetag:
	#print(img)


	
#print (imagetag)
#for image in soup.find_all('img'):
	#print(image.contents)

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
import re
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
base_url="https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"
pagelist=['']
totallinklist=[]
for i in range(1,6):
	page="&page="+str(i)
	pagelist.append(page)
#print(pagelist)
def links(url):
	req=urllib.request.Request(url, None, {'User-Agent': 'SI_CLASS'})
	fhand=urllib.request.urlopen(req,context=ctx)
	html=fhand.read()
	#print(html)
	soup=BeautifulSoup(html,'html.parser')
	linklist=[]
	for i in soup.find_all(class_="field-item"):
		try:
			if i.a.text=="Contact Details":
				path=i.a.get('href')
				link='https://www.si.umich.edu'+path
				linklist.append(link)		
		except:
			continue
	return linklist
for page in pagelist:
	url=base_url+page
	totallinklist+=links(url)
number=0
pref=len('href="mailto:')
for link in totallinklist:
	number+=1
	#print(str(number)+": "+link)
	req=urllib.request.Request(link, None, {'User-Agent': 'SI_CLASS'})
	fhand=urllib.request.urlopen(req,context=ctx)
	html=fhand.read()
	soup=BeautifulSoup(html,'html.parser')
	for i in soup.find_all(class_="field-item"):
		try:
			text=i.a.text
			if re.search('[\w-]+@([\w-]+\.)+[\w-]+',text):
				print(str(number)+" "+text)
		except:
			continue
	#for word in html:
		#if re.search('[\w-]+@([\w-]+\.)+[\w-]+',word):
			#print(word[pref+1:)
