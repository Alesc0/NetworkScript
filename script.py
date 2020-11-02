import nmap
import time
from pushbullet import Pushbullet
pb = Pushbullet('o.GJfjdZia1g0AWnBlnprlydeP24M0K2fM')

n = 0
hosts_list = []
last_list = []

while True:
    time.sleep(1)
    n = len(hosts_list)

    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.1.1/24', arguments='-R -sP -PE')
    hosts_list = [(nm[x]['hostnames'][0]['name'],x, nm[x]['status']['state']) for x in nm.all_hosts()]
    
    for x in hosts_list :
            if(x not in last_list):
                print(x[0] + " CONNECTED")
                """ push = pb.push_note("Connected", "IP CONNECTED") """
            if(x not in hosts_list):
                print(x[0] + " DISCONNECTED")
                """ push = pb.push_note("Disconnected", "IP DISCONNECTED") """
    
    print("........")
    print("........")

    last_list = hosts_list
