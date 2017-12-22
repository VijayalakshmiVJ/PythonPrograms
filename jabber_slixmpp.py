import logging
import asyncio
import datetime
import time
from slixmpp import ClientXMPP
from slixmpp.exceptions import IqError, IqTimeout

@asyncio.coroutine
def asleep(t):
    yield from asyncio.sleep(t)

def calc_smth():
    return time.mktime(datetime.datetime.now().timetuple())

class EchoBot(ClientXMPP):

    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.session_start)
        self.register_plugin('xep_0199')
    def session_start(self, event):
        try:
            self.send_presence()
        except IqError as err:
            self.disconnect()
        except IqTimeout:
            self.disconnect()


    def disconnected(self, event):
        print("%s disconnect" % self.jid)

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR,format='%(levelname)-8sessage)s')
    try:
        xmpp =  EchoBot('bot@example.com', 'password')
        xmpp.connect(address=("IM&P IP", 5222))
        xmpp.process(timeout=0.1)
        while True:
            asyncio.get_event_loop().run_until_complete(asleep(5))
            xmpp.send_message(mto='johndoe@example.com', mbody="Timestamp={}".format(calc_smth()), mtype='chat')
    except (KeyboardInterrupt, SystemExit):
        xmpp.disconnect()
        print("Done")
