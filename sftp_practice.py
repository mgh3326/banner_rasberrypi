import paramiko
paramiko.util.log_to_file('./tmp/paramiko.log')

# Open a transport

host = "52.79.178.178"
port = 22
transport = paramiko.Transport((host, port))

# Auth

k = paramiko.RSAKey.from_private_key_file("../공개키/mgh2964.pem")

username = "ubuntu"
transport.connect(username=username, pkey=k)

# Go!

sftp = paramiko.SFTPClient.from_transport(transport)

# Download

filepath = '/home/ubuntu/foo.txt'
localpath = './tmp/download.txt'
sftp.get(filepath, localpath)

# Upload

filepath = '/home/ubuntu/foo.txt'
localpath = './test.txt'
sftp.put(localpath, filepath)

# Close

sftp.close()
transport.close()


# 출처: http://mousehelp.tistory.com/5 [마우스는거들뿐]
