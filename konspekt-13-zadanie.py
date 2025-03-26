1

from ipaddress import *

net = ip_network('202.75.38.152/255.255.255.248')
for i in net:
    ip = f'{i:b}'
    if '111' in ip:
        print(ip)
   


4

from ipaddress import *
c = 0
net = ip_network('158.132.161.128/255.255.255.128')
for i in net:
    ip = f'{i:b}'
    if ip[-1] == '1':
        c = c + 1
print(c)


5

from ipaddress import *
net = ip_network('115.198.0.0/255.254.0.0')
c = 0
for i in net:
    ip = f'{i:b}'
    if ip.count('1') % 5 == 0:
        c += 1
print(c)


2

from ipaddress import *

for mask in range(33):
    net = ip_network(f'111.81.208.27/{mask}', 0)
    print(net, net.netmask)


3

from ipaddress import *

for mask in range(33):
    net = ip_network(f'215.181.200.27/{mask}', 0)
    print(net, net.netmask)


c = 0
from ipaddress import *
net = ip_network('202.75.38.160/255.255.255.240')
for i in net:
    ip1 = f'{i:b}'
    if '111' in ip1:
        c+=1
        print(ip1, c)
