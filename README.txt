This is a very simple ftp server, based on http://code.google.com/p/pyftpdlib/

Tested with python 2.4.4, should run on all 2.x versions.

Tested on windows, should be easy to use as a linux version with few modifications.

WARNING: This script is only experimental, no security at all, and btw. don't use FTP for anything.

Quickstart:
----------

Start "ftpserver.cmd", which will start the ftp server on port 21.
it will display the username and a random password, which will be different each time.

Data goes to the ./data subdir.

Use Ctrl-C to stop the server.

Copyright:
---------

Please respect the copyright of pyftpdlib, see the license file in "./pyftpdlib/".

This project has  "ftpserver.py" itself is MIT licenced, see file ./ LICENCE without any guarantee at all.


Motivation:
----------

If you need a quick and easy way to copy files between linux and nt machines in secured environemnts.
