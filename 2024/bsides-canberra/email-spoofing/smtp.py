from socket import *

mail_server = ("tantotesting.mail.protection.outlook.com", 25)
client_socket = socket(AF_INET, SOCK_STREAM)

helo = "helo tantomail.com"
mail_from = "mail from: <testing@tantomail.com>"
rcpt_to = "rcpt to: <john.doe@tantotesting.onmicrosoft.com>"
mail = """from: \x1f <,><testing@tantomail.com>\r   
sender: "James Bond" <james.bond@tantotesting.onmicrosoft.com>\r
to: <john.doe@tantotesting.onmicrosoft.com>\r
subject: Test\r
content-type: text/html\r\n\r
<!-- BEGIN PGP MESSAGE -->\r
<p>Test</p>\r
."""

def connect():
    client_socket.connect(mail_server)
    recv = client_socket.recv(1024).decode()
    print(recv)
    if recv[:3] != "220":
        print("Connection to mail server failed")
        exit()

def send(command):
    client_socket.send(f"{command}\r\n".encode())
    recv = client_socket.recv(1024).decode()
    print(recv)
    if recv[:3] != "250" and recv[:3] != "354" and recv[:3] != "221":
        print("Error with command")
        exit()

connect()
send(helo)
send(mail_from)
send(rcpt_to)
send("data")
send(mail)
send("quit")