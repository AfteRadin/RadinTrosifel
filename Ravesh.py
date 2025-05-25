import subprocess
import sys
from pyfiglet import figlet_format
from colorama import Fore, Back, Style
from os import sys
from os import system
from time import sleep	
from datetime import datetime

green="\033[1;92m"
red ="\033[1;91m"
blue="\033[1;94m"
pink="\033[1;95m"
yellow="\033[1;93m"
white="\033[1;00m"
OF = "\033[0m"
ww = "\033[0;100m"

def install_libraries():
    libraries = [
        "hashlib",
        "random",
        "base64",
        "pycryptodome",
        "ras",
        "pyruby",
        "os",
        "platform",
        "time",
        "sys",
        "subprocess",
        "requests",
        "os",
        "colorama",
        "binascii",
        "Crypto.Cipher",
        "Crypto.Util.Padding"
    ]
    for library in libraries:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])

def run_script(script_name):
    subprocess.run([sys.executable, script_name])

def main_menu():
    while True:
        print(red+figlet_format("Ravesh Ha"))
        sleep(0.5)
        print()
        print()
        print(Fore.BLUE+f"""baray che chizi ravesh mikhai?""")
        print()
        print()
        print()
        sleep(0.5)
        print(Fore.GREEN+f""". Account""")
        print()
        sleep(0.5)
        print('. Qofli')
        sleep(0.5)
        print()
        print()
        choice = input(Fore.YELLOW+f"""Enter your choice: """)
        sleep(0.5)
        print()
        print(Fore.RED+f"""Created by Radin Trosifel And shadow garden""")
        
        if choice == 'Account':
            print ("ravesh dakhel un site hast : https://codetester.io/hosting/765zByDvMYUOf885GbAi/")
        elif choice == 'Qofli':
            print ("ravesh dakhel un site hast : https://codetester.io/hosting/v650D3H9APmxNMldprTc/")
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main_menu()
