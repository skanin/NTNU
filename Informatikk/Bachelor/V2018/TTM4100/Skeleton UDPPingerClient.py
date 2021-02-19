# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *

# Get the server hostname and port as command line arguments                    
host = '127.0.0.1'  # FILL IN END
port = 12000  # FILL IN END
timeout = 1  # in seconds

# Create UDP client socket
# FILL IN START     
client = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
client.settimeout(timeout)

# FILL IN END

# Sequence number of the ping message
ptime = 0

# Ping for 10 times
while ptime < 10:
    ptime += 1
    # Format the message to be sent as in the Lab description
    # data = ('Ping' + str(ptime))# FILL IN START     # FILL IN END
    data = "Ping " + str(ptime) + "   " + str(time.asctime())
    try:
        # FILL IN START

        # Record the "sent time"
        sentTime = time.time()
        # Send the UDP packet with the ping message
        client.sendto(data, (host, port))
        # Receive the server response
        message, address = client.recvfrom(1024)
        # Record the "received time"
        recvTime = time.time()
        # Display the server response as an output
        print("Address: " + address[0])
        print("Port: " + str(address[1]))
        # Round trip time is the difference between sent and received time
        print("RTT: " + str(recvTime - sentTime))

    # FILL IN END
    except:
        # Server does not response
        # Assume the packet is lost
        print("Request timed out.")
        continue

# Close the client socket
client.close()
