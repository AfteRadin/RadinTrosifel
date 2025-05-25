# Menu Script

import subprocess
import sys
from pyfiglet import figlet_format 
from colorama import Fore, Back, Style

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
        print(red+figlet_format("Moton Jolan"))
        print()
        print()
        print(Fore.GREEN+f"""1. Matn Jolan1""")
        print("2. Matn Jolan2")
        print("3. Matn Jolan3")
        print("4. Exit")
        print()
        choice = input(Fore.BLUE+f"""Enter your choice: """)
        
        if choice == '1':
            run_script('matn1.txt')
        elif choice == '2':
            run_script('Matn2.txt')
        elif choice == '3':
            run_script('matn3.txt')
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
