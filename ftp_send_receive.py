"""
	File transfer protocol used to send and receive files using FTP server.
	Use credentials to provide access to the FTP client

	Note: Do not use root username & password for security reasons
		  Create a seperate user and provide access to a home directory of the user
		  Use login id and password of the user created 
		  cwd here stands for current working directory
"""

from ftplib import FTP

ftp = FTP("192.168.0.51")  # Enter the ip address or the domain name here
ftp.login(user="root", passwd="VGp6eEA1MQo=")
ftp.cwd("/home/postgres/user/cym/")

"""
	The file which will be received via the FTP server
	Enter the location of the file where the file is received
"""


def receive_file(filename="test.txt"):
    with open(filename, "wb") as out_file:
        ftp.retrbinary("RETR " + filename, out_file.write, 1024)
        ftp.quit()


"""
	The file which will be sent via the FTP server
	The file send will be send to the current working directory
"""


def send_file(filename="test.txt"):
    with open(filename, "rb") as in_file:
        ftp.storbinary("STOR " + filename, in_file)
        ftp.quit()
