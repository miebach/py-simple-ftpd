import time
import sha
from pyftpdlib import ftpserver


def mysha(x):
  hash = sha.new(x)
  return hash.hexdigest()


username="user"

authorizer = ftpserver.DummyAuthorizer()

password = mysha((str(time.time()) + "babble"))[:7]
print "user:",username
print "password:",password

authorizer.add_user(username, password, "./data", perm="elradfmw")
#authorizer.add_anonymous(".")
ftp_handler = ftpserver.FTPHandler
ftp_handler.authorizer = authorizer
#address = ("127.0.0.1", 21) # listen only on localhost
address = ("", 21) # listen on all interfaces
ftpd = ftpserver.FTPServer(address, ftp_handler)
ftpd.serve_forever()