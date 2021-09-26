import os
from colorama import Fore, Back, Style
from colorama import init
import sys
init(autoreset=True)




with open('kwaptoutput.txt', 'a') as file:
    print('\nThis printed data will store in a file', file=file)


# Banner (kuros web app pentesting tool)
print(Fore.RED + "ll    ll   ll               ll         lll           llllllllll     llllllllllllll      ")
print(Fore.RED + "ll   ll    ll               ll        ll ll         ll         ll         ll ")
print(Fore.RED + "ll  ll     ll               ll       ll   ll        ll         ll         ll    ")
print(Fore.RED + "ll ll      ll      ll       ll      ll     ll       ll         ll         ll    ")
print(Fore.RED + "llll       ll     ll ll     ll     ll       ll      llllllllllll          ll       ")
print(Fore.RED + "llll       ll    ll   ll    ll    ll         ll     ll                    ll     ")
print(Fore.RED + "ll ll      ll   ll     ll   ll   1lllllllllllll     ll                    ll        ")
print(Fore.RED + "ll  ll     ll  ll       ll  ll   ll          ll     ll                    ll    ")
print(Fore.RED + "ll   ll    ll ll         ll ll   ll          ll     ll                    ll     ")
print(Fore.RED + "ll    ll    ll            ll     ll          ll     ll                    ll   ")
print("any illegal activity you perform and/or take part in falls on the user (you) and not the creator of the tool")
print("There will be a output file named KWAPTOUTPUT.txt")

#makes output file
#assume we have kwaptoutput.txt and wordlist.txt

# gets all inputs from user for custom auto attacks
website = (input(Fore.GREEN + "enter url/website for this scan: "))
xssops = (input(Fore.GREEN + "enter other operators here (with spaces): "))
try:
    gobusteryesno = int(input(Fore.GREEN + "would you like to run gobuster 1 = yes 2 = no  : "))
except:
    print("you need to put 1 for yes or 2 for no!")
sqlop = (input(Fore.GREEN + "enter the SQLmap operator (with spaces): "))
subop = (input(Fore.GREEN + "Enter sublist3r operator: "))
num1 = int(input(Fore.GREEN + "Enter 1 for custom nmap or 2 for pre-setup nmap: "))
if num1 == 1:
    nmapop = input(Fore.GREEN + "Enter custom nmap operator(s) -add spaces-: ")

def xssstrike():
    try:
        os.chdir("/mnt/usb/xss-strike")
        os.system(f"python3 xsstrike.py {xssops}  -u {website}")
        os.system("cd")
    except ValueError:
           raise print("oops! there was an error with xss strike!")

# starts sqlmap with input from user


def sqlmap():
    try:
        os.chdir("/mnt/usb/sqlmap")
        os.system(f"python3 sqlmap.py {sqlop} -u {website}")
    except ValueError:
        raise print("there was an error with sql map attack!")


def sublister():
    try:
        os.chdir("/mnt/usb/Sublist3r/")
        os.system(f"python3 sublist3r.py {subop} -d {website}")
    except:
        print("oops! there was a error with sublister!")



# after a shit ton of googling i found out this is the best nmap scan for a website  or you can just use the manual option
def gobuster():
    if gobusteryesno == 2:
        print("will not run gobuster")
    elif gobusteryesno == 1:
        print("gobuster will run now!")
        os.system(f"gobuster dir -u {website} -w '/mnt/usb/kwapt/wordlist.txt' ")



# presetnmap,customnmap and nmap start all work with nmap
def presetnmap():
    try:
        os.system(f"nmap --max-rate 4 --script=http-backup-finder -o KWAPTOUTPUT.txt {website}")
        os.system(f"nmap --max-rate 4 --script http-proxy-brute -p 8080 -o KWAPTOUTPUT.txt {website}")
        os.system(f"nmap --max-rate 4 -o  KWAPTOUTPUT.txt --script http-rfi-spider -p80 {website} ")
        os.system(f"nmap --max-rate 4 -o KWAPTOUTPUT.txt -p80 --script http-default-accounts {website}")
    except:
        print("Whoops there was a error with nmap!")


def customnmap():
    try:
        os.system(f"nmap -o KWAPTOUTPUT.txt {nmapop} {website}")
    except:
        print("whoops there was a issue with your operators! look over them again please.")

def nmapstart():
    if num1 == 2:
        presetnmap()
    if num1 == 1:
        customnmap()

#starts all of the attacks
xssstrike()
sqlmap()
sublister()
gobuster()
nmapstart()
