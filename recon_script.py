# Please install Colorama before running this script!!!

import subprocess
import threading
import os
import sys
from colorama import Fore, Style
import re

def verify(ip):
    if re.match("^((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3})([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", ip):
        return True
    else:
        print ("Please enter IP Address in proper format like a.b.c.d")
        return False


def nmap (ip):
    nmap_result = subprocess.check_output(["nmap", "-T4", "-A", "-p-", ip])
    print (Fore.GREEN + """"
    *************************************************
                     NMAP RESULT                     
    *************************************************""")
    print (nmap_result)
    print (Style.RESET_ALL)

def nikto (ip):
    nikto_result = subprocess.check_output(["nikto", "-h", ip])
    print (Fore.WHITE + """"
        *************************************************
                         NIKTO RESULT                     
        *************************************************""")
    print (nikto_result)
    print (Style.RESET_ALL)

def dirb (ip):
    url = "http://" + ip
    dirb_result = subprocess.check_output(["dirb", url])
    print (Fore.YELLOW + """"
        *************************************************
                         DIRB RESULT                     
        *************************************************""")
    print (dirb_result)
    print (Style.RESET_ALL)

def main():
    if len(sys.argv) != 2:
        print ("Enter python script.py <IP Address to be attacked>\n")
        return 0
    else:
        ip = sys.argv[1]

    val=verify(ip)

    if val==False:
        return 0

    t1 = threading.Thread(target=nmap, args=(ip,))
    t2 = threading.Thread(target=nikto, args=(ip,))
    t3 = threading.Thread(target=dirb, args=(ip,))

    t1.start()
    t2.start()
    t3.start()

    # t1.join()
    # t2.join()
    # t3.join()
    # #
    # print "Command Complete!!!"
    #
    # if t1.is_alive():
    #     print "T1 Alive"
    # else:
    #     print "T1 Complete"
    #
    # if t2.is_alive():
    #     print "T2 Alive"
    # else:
    #     print "T2 Complete"
    #
    # if t3.is_alive():
    #     print "T3 Alive"
    # else:
    #     print "T3 Complete"

    threads = []

    threads.append(t1)
    threads.append(t2)
    threads.append(t2)

    for t in threads:
        t.join()

main()
os.system("stty sane")
