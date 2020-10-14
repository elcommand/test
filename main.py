import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# hostname = input("Enter host IP address: ")
# username = input("Enter SSH Username: ")
password = input("Enter SSH Password: ")

hostname = '192.168.2.1'
username = 'admin'
# password = '******'
port = 22

ssh.connect(hostname, port, username, password, look_for_keys=False)
stdin,stdout,stderr = ssh.exec_command('/ip arp print')
output = stdout.readlines()
print (''.join(output))
ssh.close()