import nmap
import time
from pushbullet import Pushbullet
pb = Pushbullet('o.GJfjdZia1g0AWnBlnprlydeP24M0K2fM')

n = 0
hosts_list = []

while True:
    time.sleep(1)
    n = len(hosts_list)

    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.1.1/24', arguments='-n -R -sP -PE')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    
    if(n < len(hosts_list)):
        print("Connected")
        push = pb.push_note("Connected", "IP CONNECTED")
    elif(n > len(hosts_list)):
        print("Disconnected")
        push = pb.push_note("Disconnected", "IP DISCONNECTED")
    else:
        print(00000)
