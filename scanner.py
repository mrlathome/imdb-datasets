import requests
import os
import bs4
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def download(link,target):
    imagefile = urllib2.urlopen(link)
    with open(target,'wb') as output:
        output.write(imagefile.read())

if not os.path.isdir("./images"):
    os.mkdir("./images")    
    
if not os.path.isdir("./images/females"):
    os.mkdir("./images/females")    
    
if not os.path.isdir("./images/males"):
    os.mkdir("./images/males")

base = "http://www.imdb.com"

images = 103
        
for start in xrange(201,4000,100):
    url = base + '/search/name?gender=female&count=100&start='+str(start)        
    r = requests.get(url)    
    html = r.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    for img in soup.select('.detailed .image'):
        link = img.find('a').get('href')    
        print "opening " + str(images) + (base + link)
        r = requests.get(base + link)    
        html = r.text
        soup = bs4.BeautifulSoup(html,'html.parser')
        selector = soup.find('time')
        if selector == None:
            continue
        date = selector.get('datetime') 
        
        selector = soup.find('img',{"id":"name-poster"})    
        if selector == None:
            continue
        image = selector.get('src')
        
        images = images + 1
        
        download(image,"./images/females/"+str(images)+"+"+date+".jpg")
        print "downloaded" 
        
for start in xrange(1,4000,100):
    url = base + '/search/name?gender=male&count=100&start='+str(start)    
    r = requests.get(url)    
    html = r.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    for img in soup.select('.detailed .image'):
        link = img.find('a').get('href')    
        print "opening " + str(images) + (base + link)
        r = requests.get(base + link)    
        html = r.text
        soup = bs4.BeautifulSoup(html,'html.parser')
        selector = soup.find('time')
        if selector == None:
            continue
        date = selector.get('datetime') 
        
        selector = soup.find('img',{"id":"name-poster"})    
        if selector == None:
            continue
        image = selector.get('src')
        
        images = images + 1
        
        download(image,"./images/males/"+str(images)+"+"+date+".jpg")
        print "downloaded"               