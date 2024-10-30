import sacn
import time
from pythonosc import udp_client

IP = "127.0.0.1"   #Loopback address - run this script on the same machine hosting your buttons (must have access to LX Net)
PORT = 12321       #Default port for Companion OSC Control
UNIVERSE = 900     #The Universe that Vor is broadcasting to.

# provide an IP-Address to bind to if you want to receive multicast packets from a specific interface
receiver = sacn.sACNreceiver()
receiver.start()  # start the receiving thread

#osc setup
client = udp_client.SimpleUDPClient(IP, PORT)

# define a callback function
@receiver.listen_on('universe', universe=UNIVERSE)  
def callback(packet):  # packet type: sacn.DataPacket
	if packet.dmxStartCode == 0x00:  # ignore non-DMX-data packets
		#print(packet.dmxData)  # print the received DMX data
		client.send_message("//custom-variable/vorrecord/value", packet.dmxData[0])

# optional: if multicast is desired, join with the universe number as parameter
receiver.join_multicast(UNIVERSE)
