import os

import paramiko
t = paramiko.Transport()
class SftpConnect(object):
    def __init__(self):
        self.IP = '192.168.31.10'
        self.PORT = '5432'
        self.USERNAME = 'abc'
        self.PASSWORD = '1qaz2wsx'
        self.sftp = paramiko.SFTPClient.from_transport((self.IP,self.PORT))

    def get_connnect(self):
        remote = 't3/remote'
        locate = 't3/locate'
        self.sftp.get(remote,locate)
        self.sftp.put(locate,remote)

    def is_exist_local_path(self,locate):
        if not os._exists(locate):
            os.mkdir(locate)
        with open(locate) as f:
            f.write('')

    def is_exist_remote_path(self,remote):
        self.sftp.chdir(remote)
        if not self.sftp.getcwd():
