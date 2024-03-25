import bs4 as bs
import urllib.request
from maildeneme import MailGonder

sauce = urllib.request.urlopen("https://yuzikibinbursu.yok.gov.tr/")
soup = bs.BeautifulSoup(sauce,'lxml')
result = soup.find_all("h3")
dizi = []

for i in soup.find_all("h3"):
    #print(i.text)
    dizi.append(i.text)



#print("*"*50)

# for j in dizi:
#     print(j)

