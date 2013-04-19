import SocketServer
## 4 of lights one and they are the first 4 lights in the chain.  Each of the lights takes 4 inputs, brightness, red,green,blue
##the 5th light is a special case

import array
from ola.ClientWrapper import ClientWrapper
wrapper = ClientWrapper()

def DmxSent(state):
      wrapper.Stop()
def lights_start(bright,red,green,blue,rotate,sp):
    lights_do(0,0,0,0,0,1)
    lights_do(bright,red,green,blue,rotate,sp)
def lights_do(bright,red,green,blue,rotate,sp): # 255, 0,0,255, 175, 206
	universe = 1
	data = array.array('B')
	light_data = [bright,red,green,blue,rotate]
	normal_light = light_data[:-1]
	tmp = [data.append(x) for x in normal_light*4]
	if sp == 1 : 
        	tmp = [data.append(x) for x in light_data]



	# data = array.array('B')
	# data.append(bright)
	# data.append(red)
	# data.append(green)
	# data.append(blue)
	# data.append(bright)
	# data.append(red)
	# data.append(green)
	# data.append(blue)
	# data.append(bright)
	# data.append(red)
	# data.append(green)
	# data.append(blue)
	# data.append(bright)
	# data.append(red)
	# data.append(green)
	# data.append(blue)
	# data.append(bright)
	# data.append(red)
	# data.append(green)
	# data.append(blue)
	# data.append(rotate)
	#wrapper = ClientWrapper()
	client = wrapper.Client()
	client.SendDmx(universe, data, DmxSent)
	wrapper.Run()



	
class MyTCPHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline().strip()
        print self.data
        list_vals = [int(x) for x in self.data.split(",")]
        lights_start(*list_vals)
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write("YES")


HOST, PORT = "0.0.0.0", 9999
###lights(255, 0,0,255,255)
    # Create the server, binding to localhost on port 9999
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)


server.serve_forever()
