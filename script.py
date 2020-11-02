import nmap
import time
from pushbullet import Pushbullet
pb = Pushbullet('o.CkGvbNmkW5biq0syYmnRbe4bhJgz1OFD')

n = 0
hosts_list = []
last_list = []

while True:
    time.sleep(1)
    n = len(hosts_list)

    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.1.1/24', arguments='-R -sP -PE')
    hosts_list = [(nm[x]['hostnames'][0]['name'],x) for x in nm.all_hosts()]
    
    for x in hosts_list :
        if(x not in last_list):
            print(x[0] + "  " + x[1] + " CONNECTED")
            """ push = pb.push_note("Connected", "IP CONNECTED") """
            
    for x in last_list : 
            if(x not in hosts_list):
                print(x[0] + "  " + x[1] + " DISCONNECTED")
                """ push = pb.push_note("Disconnected", "IP DISCONNECTED") """
    
    last_list = hosts_list

    print("........")
    print("........")
