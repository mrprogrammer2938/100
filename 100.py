#!/usr/bin/python3
# This Programm Write by Mr.nope
# 100 v1.3.0
import os
import time
import sys
import platform
import webbrowser
import subprocess
try:
    from colorama import Fore,init
    init()
except ImportError:
    print("\nInstalling Colorama...")
    run_in_py_lib = subprocess.getoutput("pip3 install colorama")
system = platform.uname()[0]
End = '\033[0m'
Run_Err = "\nPlease, Run This Programm on Linux, Windows or MacOS!\n"
opt = Fore.GREEN + "\n\n100/> " + End
banner = Fore.GREEN + """
         _  ___   ___
        / |/ _ \ / _ \ 
        | | | | | | | | """ + Fore.RED + "Version: " + Fore.CYAN + "1.3.0" + Fore.GREEN + """
        | | |_| | |_| |
        |_|\___/ \___/ """ + End
def title():
    if system == 'Linux':
        os.system("printf '\033]2;100\a'")
    elif system == 'Windows':
        os.system("title 100")
    else:
        print(Run_Err)
        sys.exit()
def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print(Run_Err)
        sys.exit()
def main():
    title()
    cls()
    print(banner)
    list()
def list():
    print("\n\t{1}.Black-Tool")
    print("\t{2}.Black-Tool Termux")
    print("\t{3}.Black-Tool Windows")
    print("\t{4}.K-Tool")
    print("\t{5}.DDos Attack")
    print("\t{6}.Cryptography")
    print("\t{7}.Gmail-Brute Force")
    print("\t{8}.Hack Framework")
    print("\t{0}.More Tools")
    print("\t{99}.Exit")
    choose = input(opt)
    if choose == '1':
        cls()
        print("Installing Black-Tool")
        run_ = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Black-Tool")
        try1()
    elif choose == '2':
        cls()
        print("Installing Black-Tool")
        run_2 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Black-Tool-Termux")
        try1()
    elif choose == '3':
        cls()
        print("Installing Black-Tool")
        run_3 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Black-Tool-Windows")
        try1()
    elif choose == '4':
        cls()
        print("Installing Black-Tool")
        run_4 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/K-Tool")
        try1()
    elif choose == '5':
        cls()
        print("Installing Black-Tool")
        run_5 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/DDos-Attack")
        try1()
    elif choose == '6':
        cls()
        print("Installing Black-Tool")
        run_6 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Cryptography")
        try1()
    elif choose == '7':
        cls()
        print("Installing Black-Tool")
        run_7 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Gmail-Brute Force")
        try1()
    elif choose == '8':
        cls()
        print("Installing Black-Tool")
        run_8 =  subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Hack-Framework")
        try1()
    elif choose == '0':
        try_op()
    elif choose == '99':
        ext()
    elif choose == '' or choose == ' ':
        main()
    else:
        cls()
        print(choose + Fore.RED + " Not Found!" + End)
        try1()
def try1():
    try_to_Main_Menu = input("\npress Enter...")
    if try_to_Main_Menu == '':
        main()
    else:
        main()
def ext():
    cls()
    print(Fore.GREEN + "Exiting..." + End)
    sys.exit()
def try_op():
    print("\nOpenning Tools...\n")
    webbrowser.open_new_tab("https://mrprogrammer2938.github.io/Repositories/")
    time.sleep(1)
    try1()
if __name__ == '__main__':
    try:
        try:
            main()
        except KeyboardInterrupt:
            print("\nCtrl + C")
            print("\nExiting...")
            sys.exit()
    except EOFError:
        print("\nCtrl + D")
        print("\nExiting...")
        sys.exit()