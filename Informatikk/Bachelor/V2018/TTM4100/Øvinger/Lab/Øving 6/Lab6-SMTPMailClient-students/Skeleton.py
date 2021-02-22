# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

from socket import *
import argparse as ap
import getpass as gp
import base64

#-f "sander.b.lindberg@gmail.com" -t "sanderbl@stud.ntnu.no" -u "sander.b.lindberg@gmail.com"

# Get sender_email and recipient_email as arguments to the program
#parser = ap.ArgumentParser(description='A test SMTP client without authentication')
#parser.add_argument('-f', '--from', dest='fromMail', required=True, metavar='<sender_email>')
#parser.add_argument('-t', '--to', dest='toMail', required=True, metavar='<recipient_email>')
# If using the authentication of the SMTP server, also get a valid username (optional exercise)
#parser.add_argument('-u', '--username', dest='username', required=True, metavar='<username>')

#args = parser.parse_args()
#fromMail = args.fromMail #Sender's email address
#toMail = args.toMail #Recipient's email address
#username = args.username #SMTP username in case you are implementing the optional exercise

# If using the authentication of the SMTP server, ask for a valid password (optional exercise)
#password = gp.getpass(prompt='Password: ')
# username = "sanderbl"
# password = ""
# Message to send
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Our mail server is smtp.stud.ntnu.no but it allows only authenticated communications. (optional exercise)
mailserver = 'smtp.office365.com'  # 'smtp.stud.ntnu.no'
# You can run a local simple SMTP server such as "Fake SMTP Server" and communicate with it without authentication.
# mailserver = 'localhost'
mailPort = 587
# Create socket called clientSocket and establish a TCP connection
# (use the appropriate port) with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(30)
clientSocket.connect((mailserver, mailPort))
# Fill in end

recv = clientSocket.recv(1024)
print("1. " + recv.decode())
if recv[:3] != '220'.encode():
    print('220 reply not received from server.')

# Send HELO command and print server response.
# Can use EHLO instead since HELO is obsolete, but the latter can still be used
heloCommand = 'EHLO Hey\r\n'
clientSocket.send(heloCommand.encode())  # Python 3
# clientSocket.send(heloCommand) #Python 2.7
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("2. " + recv1)
if recv1[:3] != '250'.encode():
    print('250 reply not received from server. Yo')

'''
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())

clientSocket.send(username.encode())
clientSocket.send("\r\n".encode())
recv_user = clientSocket.recv(1024)
print("Response after sending username: " +recv_user.decode())

clientSocket.send(password.encode())
clientSocket.send("\r\n".encode())
recv_pass = clientSocket.recv(1024)
print("Response after sending password: " +recv_pass.decode())
'''
clientSocket.send(('starttls\r\n').encode())
recv_tls = clientSocket.recv(1024)
print("TLS: " + recv_tls.decode())

username = "sanderbl"
password = ""


base64_str = ("\x00"+username+"\x00"+password).encode()
#base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(4096)
print(recv_auth.decode())




'''
authMsg = "AUTH PLAIN\r\n"
clientSocket.send(authMsg.encode())
recv_auth = clientSocket.recv(1024)
print("OK?")
print("AUTH: " + recv_auth.decode())
'''



# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <sander.b.lindberg@gmail.com>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: " + recv2)

if recv1[:3] != '250'.encode():
    print('MAIL FROM: 250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptTo = 'RCPT TO: <sander.b.lindberg@gmail.com>\r\n'
clientSocket.send(rcptTo.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("4. " + recv2)
if recv2[:3] != '250'.encode():
    print('RCPT TO: 250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = 'DATA\r\n'
clientSocket.send(data.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("5. " + recv1)
if recv1[:3] != '354'.encode():
    print('DATA: 250 reply not received from server.')

# Fill in end

# Send message data.
# Fill in start
msg = '\r\n'
clientSocket.send(msg.encode())
clientSocket.send('Very important message!\r\n')
# Fill in end

# Message ends with a single period.
# Fill in start
endMsg = '.\r\n'
clientSocket.send(endMsg.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("6. " + recv1)
if recv1[:3] != '250'.encode():
    print('END: 250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitMsg = 'QUIT\r\n'
clientSocket.send(quitMsg.encode())
clientSocket.close()
pass
# Fill in end

# Note that there are more communications if you implement the optional exercise.
