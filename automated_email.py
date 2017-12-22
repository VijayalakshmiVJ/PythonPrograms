# Sending automated emails

import smtplib

TO = ['lohith.k_n@nokia.com', 'vijayalakshmi.s@nokia.com', 'naveen.kumar_s@nokia.com', 'manjurekha.venkatesan@nokia.com','priyadarshni.j@nokia.com', 'arun.s.s@nokia.com']
FROM = ['akshay.murgod@nokia.com']
smtpObj = smtplib.SMTP('dhn-mailrelay.emea.nsn-intra.net',25)
#type(smtpObj)

#smtpObj.connect("mail.emea.nsn-intra.net",465)

#smtpObj.ehlo()

#smtpObj.starttls()

#smtpObj.login(' vijayalakshmi.s@nokia.com ', ' 19Almostthere89 ')

#msg = """\
#        From: %s
#        To: %s
#        Subject: %s
#
#       %s
#        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

smtpObj.sendmail(FROM, TO, 'Subject: Lunch treat in Nagarjuna tomorrow!\nHello,\n\n   Lets go to Nagarjuna tomorrow , my treat. No occasion , just like that :)')
smtpObj.quit()


