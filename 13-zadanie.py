# дан адрес узла и маска
# просят найти ip-адресы узлов в этой сети,
# удовлетворяющие условию

# from ipaddress import *

# net = ip_network('адрес сети/адрес маска')
# for i in net:
#     ip1 = f'{i:b}'
#     '/'
#     ip2 = bin(int(i))[2:].zfill(32)
#     if # условие


# дан адрес узла и адрес сети
# просят найти маску

# from ipaddress import *

# for mask in range(33):
#     net = ip_network(f'адрес узла/{mask}', 0)
#     print(net, net.netmask)

    # далее ищем ответ на вопрос в терминале







# from ipaddress import *
# net  =  ip_network('202.75.38.152/255.255.255.248')
# for i in net:
#     ip = f'{i:b}'
#     if '111' in ip:
#         print(ip)


# for mask in range(33):
#     net = ip_network(f'111.81.208.27/{mask}', 0)
#     print(net, net.netmask)


# for mask in range(33):
#     net = ip_network(f'215.181.200.27/{mask}', 0)
#     print(net, net.netmask)

# from ipaddress import *
# c= 0
# net = ip_network('158.132.161.128/255.255.255.128')
# for i in net:
#     ip = bin(int(i))[2:].zfill(32)
#     if ip[-1] == '1':
#         c+=1
# print(c)


# from ipaddress import *
# c= 0
# net = ip_network('115.198.0.0/255.254.0.0')
# for i in net:
#     ip = bin(int(i)).zfill(32)
#     if ip.count('1')%5==0:
#         c+=1
# print(c)


# from ipaddress import *
# c = 0
# net = ip_network('112.160.0.0/255.240.0.0')
# for i in net:
#     ip = bin(int(i)).zfill(32)
#     if ip.count('1')%3!=0:
#         c+=1
# print(c)

# from ipaddress import *
# c = 0
# net = ip_network('192.168.32.160/255.255.255.240')
# for i in net:
#     ip =  bin(int(i))[2:].zfill(32)
#     if ip.count('0')>21:
#         c+=1
# print(c)


# from ipaddress import *
# for mask in range(32, 0, -1):
#     net = ip_network(f'154.63.206.129/{mask}', 0)
#     if ip_address('154.63.100.75') in net:
#         c = 0
#         for ip in net:
#             n = bin(int(ip))[2:].zfill(32)
#             if n.count('1')%2==0:
#                 c+=1
#         print(c)
#         break


# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'98.162.198.94/{mask}', 0)
#     print(net, net.netmask)


# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'98.162.71.94/{mask}', 0)
#     print(net, net.netmask)

# print(bin(192)[2:], bin(224)[2:])
# print(2**14)

# from ipaddress import *
# net = ip_network('237.195.158.37/255.255.192.0', 0)
# print(net)

# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'98.162.71.151/{mask}', 0)
#     if ip_address('98.162.71.155') in net:
#         c = 0
#         for i in net:
#             ip  = bin(int(i))[2:].zfill(32)
#             print(ip.count('1'))
#             break

# from ipaddress import *

# for mask in range(32 + 1):
#   net1 = ip_network(f'98.162.71.151/{mask}', 0)
#   net2 = ip_network(f'98.162.71.155/{mask}', 0)
#   if net1 != net2:
#     print(net1)


# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'98.162.71.94/{mask}', 0)
#     print(net, net.netmask)

# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'208.172.216.35/{mask}', 0)
#     print(net, net.netmask)

# print(2**(32-21))

# from ipaddress import *
# c = 0
# net = ip_network('203.153.0.0/255.255.0.0', 0 )
# for i in net:
#     ip = bin(int(i))[2:].zfill(32)
#     if ip[-1]=='0':
#         c+=1
# print(c)


# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'221.175.29.68/{mask}', 0)
#     if ip_address('221.175.5.70') in net:
#         print(net, net.netmask)

# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'119.167.50.77/{mask}', 0)
#     print(net, net.netmask)


# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'128.175.95.31/{mask}', 0)
#     if ip_address('128.175.96.13') in net:
#         print(net, net.netmask)

# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'111.81.88.168/{mask}', 0)
#     print(net, net.netmask)

# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'245.166.144.200/{mask}', 0)
#     print(net, net.netmask)

# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'128.175.95.31/{mask}', 0)
#     if ip_address('128.175.96.13') in net:
#         print(net, net.netmask)