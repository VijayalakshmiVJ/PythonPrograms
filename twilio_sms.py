#SMS

from twilio.rest import TwilioRestClient

accountSID = 'AC6fb9ce9413800fd5974c5c9d04e6b99f'
authToken = '26431291c4692f2fe8cd2f61749a7142'

twilioCli = TwilioRestClient(accountSID, authToken)

print('Twilioongoing')
myTwilioNumber = '+18565170259'
myCellPhone = '+919008111210'

print('Sendingmsg')
message = twilioCli.messages.create(body='VJ your first python SMS is here', from_=myTwilioNumber, to=myCellPhone)

print(message.status)
