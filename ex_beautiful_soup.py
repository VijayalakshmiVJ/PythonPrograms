
import requests, bs4

res = requests.get('http://automatetheboringstuff.com', auth=('user', 'pass'), timeout=5)
#res.raise_for_status()
#noStarchSoup = bs4.BeautifulSoup(res.text)
#type(noStarchSoup)
