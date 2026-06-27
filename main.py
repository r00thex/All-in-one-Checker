import os
import sys
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

logo = f"""{Fore.CYAN}
  _____ _                 ____ _               _             
 |_   _| |__   ___       / ___| |__   ___  ___| | _____ _ __ 
   | | | '_ \ / _ \_____| |   | '_ \ / _ \/ __| |/ / _ \ '__|
   | | | | | |  __/_____| |___| | | |  __/ (__|   <  __/ |   
   |_| |_| |_|\___|      \____|_| |_|\___|\___|_|\_\___|_|   
                                                             
        {Fore.YELLOW}developer by Root_hex- The Checker
{Style.RESET_ALL}
"""

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"{Fore.CYAN}[1] {Fore.WHITE}cPanel Checker")
        print(f"{Fore.CYAN}[2] {Fore.WHITE}WordPress Checker")
        print(f"{Fore.CYAN}[3] {Fore.WHITE}Gmail Checker")
        print(f"{Fore.CYAN}[4] {Fore.WHITE}Proxy Checker")
        print(f"{Fore.CYAN}[0] {Fore.RED}Keluar")
        print()

        choice = input(f"{Fore.YELLOW}[?] Select menu: {Fore.WHITE}")
        
        if choice == "1":
            os.system("python cPanel-Checker.py")
        elif choice == "2":
            os.system("python Wp-Checker.py")
        elif choice == "3":
            os.system("python G-U-Checker.py")
        elif choice == "4":
            os.system("python Proxy-Checker.py")
        elif choice == "0":
            print(f"{Fore.RED}[!] Exit....")
            sys.exit()
        else:
            print(f"{Fore.RED}[!] Invalid selection!")
            input(f"{Fore.YELLOW}[ENTER] Back to menu...")

if __name__ == "__main__":
    main_menu()
