#!/usr/bin/python

"""
Snap!BYOB extension to interact with Raspberry Pi GPIO
through mrra and upm libs.
Python serversocket.
Author G. Vidal <gerard.vidal@ens-lyon.fr>

Snap!BYOB blocks are provided by RPiGPIOmraa.xml

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import socketserver
import mraa, time
import re

class SnRPiHTTPRqHandler(socketserver.BaseRequestHandler):
	
	def handle(self):
		# self.request is the TCP socket connected to the client
		self.data = self.request.recv(2048).strip()
		strData = str(self.data)
		# just send back 'OK'
		if strData.endswith("keep-alive'"):
			self.request.sendall(str.encode('OK'))
		print (self.data)
		reObj = re.compile(".*pin=([0-9]*).*state=(LOW|HIGH|INF)")
		reMatch = reObj.match(str(self.data))
		self.pin = int(reMatch.group(1))
		print ('Pin activated : {}'.format(self.pin))
		led = mraa.Gpio(self.pin)
		led.dir(mraa.DIR_OUT)
		led.write(1)
		if reMatch.group(2) == 'LOW':
			led.write(0)
		elif reMatch.group(2) == 'HIGH':
			led.write(1)
			time.sleep(10)
		else :
			led.dir(mraa.DIR_IN)

	
def main():
	try:
		HOST, PORT = '', 8185
		Handler = SnRPiHTTPRqHandler
		
		with socketserver.TCPServer((HOST, PORT), Handler)  as server:
			
			print ('serving at port : {}'.format(PORT))
			print ('Use custom Rpi blocs in Snap!')
			server.serve_forever()
	except KeyboardInterrupt:
		print ('Stop Request received, shutting down server')
		server.socket.close()

if __name__ == '__main__':
    main()


