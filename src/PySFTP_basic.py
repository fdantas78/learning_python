'''
Created on Jun 6, 2017

@author: makaidaimyo
'''

'''
pip install pycrypto
pip install paramiko
pip install pysftp
'''
import pysftp as sftp

def push_file_to_server():
    s = sftp.Connection(host='138.197.151.242',
                        username='root',
                        password='')
    local_path = "test_file.txt"
    remote_path = "/home/test_file.txt"
    
    s.put(local_path, remote_path)
    s.close()
    
#push_file_to_server()

def get_file_from_server():
    s = sftp.Connection(host='138.197.151.242',
                        username='root',
                        password='')
    local_path = "test_file.txt"
    remote_path = "/home/test_file.txt"
    s.get(remote_path, local_path)
    s.close()
    
get_file_from_server()