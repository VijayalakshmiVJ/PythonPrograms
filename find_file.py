
import os, time
import glob
import smtplib

print('Enter imsgw path directory of your local compilation')
path = input()
print('Enter your email ID')
email = input()
TO = [email]
FROM = ['Your_Personal_laptop@nokia.com']
smtpObj = smtplib.SMTP('dhn-mailrelay.emea.nsn-intra.net',25)

for infile in glob.glob( os.path.join(path, 'log*') ):
    print ('current file is: ' + infile)
    
print('Tracking compilation')
def tracker():
    if 'IMSGW Build Ended' in open(infile).read():
        print('Its finished')
        if 'Compilation failure' in open(infile).read():
            print('Compilaton done, FAILURE sending mail')
            smtpObj.sendmail(FROM, TO, 'Subject: Local Compilation Done!\nHello,\n\n   Greetings from your personal Laptop\n\n   Unfortunately your Local compilation was a FAILURE!! Please check!')
        else:
            print('Compilaton done, SUCCESS sending mail')
            smtpObj.sendmail(FROM, TO, 'Subject: Local Compilation Done!\nHello,\n\n   Greetings from your personal Laptop\n\n  Your Local compilation was a Success!! ')
        smtpObj.quit()

    else:
        return 'No'


while tracker() == 'No':
    #print('Sleeping for 5 mins and checking again')
    time.sleep(300)




        

    
    

    




