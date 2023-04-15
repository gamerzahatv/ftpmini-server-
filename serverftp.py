from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(ip_address)
try:
	authorizer = DummyAuthorizer()
	authorizer.add_user("admin", "admin", "/root/ftp/File", perm="elradfmw")
	authorizer.add_anonymous(os.getcwd())

	handler = FTPHandler
	handler.authorizer = authorizer
	address = ('ip_address',66)
	server = FTPServer((address), handler)
	server.serve_forever()
except Exception as e:  #you can specify type of Exception also
	print(e)
	quit()
	




