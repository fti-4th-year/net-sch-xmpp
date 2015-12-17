import zmq
import time
import sys
import random
import re
from threading import Thread
from time import sleep
port =  sys.argv[ 1 ]
int( port )
context = zmq.Context()
socket = context.socket( zmq.REQ )
socket.connect( "tcp://localhost:%s" % port )
socket.send( "request" )
message = socket.recv()

tmpstr = re.search( "<body>.*</body>" , message ).group(0).replace( "<body>" , "" ).replace( "</body>" , "" )

print tmpstr
