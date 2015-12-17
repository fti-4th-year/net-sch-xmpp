import xmpp
import urllib2
import time
import random
import re
import zmq
import sys

username = 'username'
passwd = 'password'
to='name@example.com'

port =  sys.argv[ 1 ]
int( port )
context = zmq.Context()
socket = context.socket( zmq.REP )
socket.bind( "tcp://*:%s" % port )

def getTemp():
	response = urllib2.urlopen( 'http://weather.nsu.ru/loadata.php?tick=%i&rand=%d&std=three' % ( round( time.time() / 1000.0 ) , random.random() ) )
	body = response.read()
	tmpstr1 = re.search( "window\.document\.title.*" , body )
	tempmsg = re.search( "[-+]*[0123456789]\.[0123456789]" , tmpstr1.group(0) ).group(0)
	return tempmsg
while True:
	message = socket.recv()
	#tempmsg = tmpstr.group( 0 ).replace( "window.document.title = " , "" ).replace( "'" , "" ).replace( ";" , "" )
	message = xmpp.Message( to , getTemp() )
	message.setAttr( 'type', 'weather')
	#message.setAttr( 'xmlns', 'custom')
	socket.send( str( message ) )
