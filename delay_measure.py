from mininet.net import Mininet
from mininet.topo import LinearTopo

# Create topology
topo = LinearTopo(k=5)
net = Mininet(topo)

net.start()

h1 = net.get('h1')
h5 = net.get('h5')

print("Measuring delay between h1 and h5...")
result = h1.cmd('ping -c 5 ' + h5.IP())

print(result)

net.stop()