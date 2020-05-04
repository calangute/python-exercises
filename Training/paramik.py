'''
Created on Feb 1, 2017

@author: empqtut
'''
import paramiko

def mySSHClient(server, port=22, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(server, port, user, password)
    except paramiko.SSHException:
        raise RuntimeError("Connection Failed")
        
    return client

ssh = mySSHClient(server='193.101.144.143', username='systch1',password='ChTeam123')
sftp = ssh.open_sftp()