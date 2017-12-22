
#! python3

import http.client
import urllib.request


#h1 = http.client.HTTPConnection('nokiameetings.webex.com')
#h1.connect()

#response = urllib.request.urlopen("https://nokiameetings.webex.com/mw3100/mywebex/default.do?siteurl=nokiameetings&main_url=%2Fmw3100%2Fmywebex%2Floginframe.do%3Fsiteurl%3Dnokiameetings%26rightlink%3D%252Fmw3100%252Fmywebex%252Fcmr%252Fmypmr.do%253Fsiteurl%253Dnokiameetings%2526frommenu%253Dtrue%2526logfrom%253D2&service=10").read()

#html = response.read()

#print(html)

with urllib.request.urlopen('https://nokiameetings.webex.com/mw3100/mywebex/default.do?siteurl=nokiameetings&main_url=%2Fmw3100%2Fmywebex%2Floginframe.do%3Fsiteurl%3Dnokiameetings%26rightlink%3D%252Fmw3100%252Fmywebex%252Fcmr%252Fmypmr.do%253Fsiteurl%253Dnokiameetings%2526frommenu%253Dtrue%2526logfrom%253D2&service=10') as response:
   html = response.read()

#print(html)

   

