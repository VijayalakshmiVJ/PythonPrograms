# Retreiving mails and reading them from outlook


import os, sys
import win32com.client
from datetime import datetime
from datetime import timedelta
import pywintypes

 
OLE_TIME_ZERO = datetime(2017, 4, 19, 0, 0, 0)
def ole2datetime(oledt):
    return OLE_TIME_ZERO + timedelta(days=float(oledt))

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(3) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder

messages = inbox.Items
message = messages.GetLast()
body_content = message.body
print(body_content)

#message.Delete()
