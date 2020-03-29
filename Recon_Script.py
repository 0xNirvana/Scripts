# P.S. BEFORE RUNNING THIS SCRIPT PLEASE INSTALL MODULES PYFIGLET AND COLORAMA USING THE COMMAND
# pip install pyfiglet
# pip install colorama

import subprocess                   # To execute all the commands like nikto, nmap, dirb
import threading                    # Used to create threads so that all the searches can run simultaneously
import os                           # Used at the last command else the terminal was breaking i.e. script ran properly but after execution whatever was written on terminal didn't didn't get displayed and 'reset' command was need to make the terminal normal
import sys                          # Used to capture the arguements passed when the script gets executed
from colorama import Fore, Style    # Used to color the output
import re                           # Used for regex to check if the IP address entered is in proper format
import pyfiglet                     # Used to get those ASCII Art Banners

def verify(ip):
    if re.match("^((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3})([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", ip):
        return True
    else:
        print ("Please enter IP Address in proper format like a.b.c.d")
        return False


def nmap (ip):
    nmap_result = subprocess.check_output(["nmap", "-T4", "-A", "-p-", ip])
    print (Fore.GREEN)                                                          # Set the color of the output
    print (pyfiglet.figlet_format("NMAP RESULTS"))                              # Prints the banner
    print (nmap_result)
    print (Style.RESET_ALL)                                                     # Resets the color style

def nikto (ip):
    nikto_result = subprocess.check_output(["nikto", "-h", ip])
    print (Fore.WHITE)
    print (pyfiglet.figlet_format("NIKTO RESULTS"))
    print (nikto_result)
    print (Style.RESET_ALL)

def dirb (ip):
    url = "http://" + ip
    dirb_result = subprocess.check_output(["dirb", url])
    print (Fore.YELLOW)
    print (pyfiglet.figlet_format("DIRB RESULTS"))
    print (dirb_result)
    print (Style.RESET_ALL)

def main():
    if len(sys.argv) != 2:                                                  #Check if 2 args are passed i.e. script_name.py and IP Address
        print ("Enter python script.py <IP Address to be attacked>\n")
        return 0
    else:
        ip = sys.argv[1]                                                    #Assigning IP address arguement to ip

    val=verify(ip)

    if val==False:
        return 0

    #Creating thread processes
    t1 = threading.Thread(target=nmap, args=(ip,))
    t2 = threading.Thread(target=nikto, args=(ip,))
    t3 = threading.Thread(target=dirb, args=(ip,))

    # Starting the thread Processes
    t1.start()
    t2.start()
    t3.start()

    threads = []

    # Appending the threads in a queue to print them in a sequence
    threads.append(t1)
    threads.append(t2)
    threads.append(t2)

    # Joining the threads in the sequence they are appended
    for t in threads:
        t.join()

main()
os.system("stty sane")                          # To avoid breaking the terminal
