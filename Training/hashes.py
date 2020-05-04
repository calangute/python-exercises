'''
Created on Feb 28, 2017

@author: empqtut
'''
import paramiko



trans = paramiko.Transport("193.101.144.178")

trans.connect(username="systch1",password="ChTeam123")

sftp = paramiko.SFTPClient.from_transport(trans)

fils = sftp.stat("/home/systch1/java0.log")