from bs4 import BeautifulSoup
import re
import urllib.request as urllib2
import os
import json
import urllib.request

# url of amazon products (should be the 2nd page)

url="https://www.amazon.in/s?k=shirt&i=apparel&page=2&qid=1594640018&ref=sr_pg_2"
page_no=2           #Specify how many images you want to scrap
txt_name="search_urls.txt"
output_path="output"

header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

f = open(txt_name, 'w+')

for page in range(1,page_no+1):
    url2=re.sub(r'(?<=&page=).+?(?=&)', str(page), url)
    soup = get_soup(url2,header)
    parsed=soup.find_all("img",{"class":"s-image"})#"rg_i Q4LuWd"
    for link in parsed:
        img_url=link.get('src')
        f.write(img_url)
        f.write('\n')
f.close()    

if not os.path.exists(output_path):
    os.mkdir(output_path)
        
with open(txt_name, 'r') as urllist:
    links=urllist.read().splitlines()
    for i in range(len(links)):
        urllib.request.urlretrieve(links[i], os.path.join(output_path, str(i)+".jpg"))
#d=urllib.request.urlretrieve("https://m.media-amazon.com/images/I/916bHFDRGfL._AC_UL320_.jpg", "00000001.jpg")