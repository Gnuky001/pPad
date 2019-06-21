import requests
from bs4 import BeautifulSoup

proxyDomain = "https://free-proxy-list.net/"
r = requests.get(proxyDomain)
soup = BeautifulSoup(r.content, "html.parser")
table = soup.find("table", {"id" : "proxylisttable"})

for row in table.find_all("tr"):
    cols = row.find_all("td")
    try:
        print "%s:%s\t%-40s\t%-50s" % (cols[0].get_text(), cols[1].get_text(), cols[3].get_text(), cols[4].get_text())
    except:
        pass