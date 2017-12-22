import requests, sys, webbrowser, bs4


res = requests.get('https://nokiameetings.webex.com/mw3100/mywebex/default.do?siteurl=nokiameetings&rnd=0.05897276889154168')
res.raise_for_status()
#playFile = open('/exe/T31L/webex/,nokiameetings,60472030081845428,524181412,MC,1-1-0,SDJTSwAAAAQdGAFXnyPQXoQNR_QfxvHpasPH_iWzJlw135z22j3Ejw2_webex.exe', 'wb')

#for chunk in res.iter_content(100000):
 #       playFile.write(chunk)


#with open("/exe/T31L/webex/,nokiameetings,60472030081845428,524181412,MC,1-1-0,SDJTSwAAAAQdGAFXnyPQXoQNR_QfxvHpasPH_iWzJlw135z22j3Ejw2_webex.exe", "wb") as code:
#    code.write(r.content)

soup = bs4.BeautifulSoup(res.content)
#linkElems = soup.select('btn btn-success a')
#webbrowser.open('http://google.com' + linkElems.get('href'))
