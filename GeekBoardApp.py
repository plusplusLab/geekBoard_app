# #3>> import struct
# 3>> print(struct.pack('>B', 0))
# b'\x00'
# 3>> print(struct.pack('>B', 255))
# b'\xff'
# 3>> print(struct.pack('>2B', 255, 0))
# b'\xff\x00'
# 3>> print(struct.pack('>H', 9000))
# b'#('
#
# So what you really want is:
#
# data = arduino.write(struct.pack('>B', valueToWrite))

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from string import split
import logging
import GeekBoard
import sys


class GetHandler(BaseHTTPRequestHandler):

    port = 50209

    def do_GET(self):

        # skip over the / in the command

    #    if self.path != "/poll":
        #print self.path

        #cmd = self.path[1:]
        # create a list containing the command and all of its parameters
        #cmd_list = split(cmd, '/')

        if self.path == '/poll':
            resp = ''
            for i in range(4):
                if board.getActiveAnalog(i) == 1:
                    #print "analogPin" + '%d'%(i+1) + "is active"
                    # get the pin value
                    val  = 512
                    resp = resp + "ar/1 " + '%d'%val + '\n'
                    val = 127
                    resp = resp + "ar/2 " + '%d'%val + '\n'
            self.send_resp(resp)

            #val = board.getAnalogValue(0)





    def send_resp(self, response):
        """
        This method sends Scratch an HTTP response to an HTTP GET command.
        """

        crlf = "\r\n"
        #http_response = str(response + crlf)
        http_response = "HTTP/1.1 200 OK" + crlf
        http_response += "Content-Type: text/html; charset=ISO-8859-1" + crlf
        #http_response += "Content-Length" + str(len(response)) + crlf
        http_response += "Access-Control-Allow-Origin: *" + crlf
        http_response += crlf
        #add the response to the nonsense above
        if response != 'okay':
            http_response += str(response + crlf)
            print http_response
        # send it out the door to Scratch
        self.wfile.write(http_response)



serial = str(sys.argv[1]);
board = GeekBoard.GeekBoard()
board.initGeekBoard(serial)

if __name__ == "__main__":

    try:
        server = HTTPServer(('localhost', 50209), GetHandler)
        print ' La GeekBoard est up and running'
        print 'Control + C pour stopper \n'
        print 'Maintenant demarrez Scratch 2.0 offline'
    except Exception:

        print 'Le port est peut etre deja utilise'
        raise
    try:
        #start the server
        server.serve_forever()
    except KeyboardInterrupt:

        print "A bientot"
        raise KeyboardInterrupt
