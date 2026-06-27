import requests
import socks
import socket
import concurrent.futures
import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

logo = f"""{Fore.CYAN}
  ____                             ____ _               _             
 |  _ \ _ __ _____  ___   _       / ___| |__   ___  ___| | _____ _ __ 
 | |_) | '__/ _ \ \/ / | | |_____| |   | '_ \ / _ \/ __| |/ / _ \ '__|
 |  __/| | | (_) >  <| |_| |_____| |___| | | |  __/ (__|   <  __/ |   
 |_|   |_|  \___/_/\_\\__,  |      \____|_| |_|\___|\___|_|\_\___|_|   
                      |___/                                           
{Style.RESET_ALL}       {Fore.GREEN}By Roothex - Proxy Billa Style.RESET_ALL}
"""

print(logo)

print(f"{Fore.CYAN}[1] Check HTTP/S Proxy{Style.RESET_ALL}")
print(f"{Fore.CYAN}[2] Check SOCKS4 Proxy{Style.RESET_ALL}")
print(f"{Fore.CYAN}[3] Check SOCKS5 Proxy{Style.RESET_ALL}")
print(f"{Fore.CYAN}[4] Check Proxy with authentication (user:pass){Style.RESET_ALL}")
mode = input(f"{Fore.CYAN}[?] Select Mode (1/2/3/4): {Style.RESET_ALL}")

file_path = input(f"{Fore.CYAN}[?] Enter proxy list file name (.txt): {Style.RESET_ALL}")

if not os.path.exists(file_path):
    print(f"{Fore.RED}[!] File not found: {file_path}{Style.RESET_ALL}")
    exit()

with open(file_path, "r", encoding="utf-8") as f:
    proxies = [line.strip() for line in f.readlines() if line.strip()]

valid_proxies = []

def check_http_proxy(proxy):
    try:
        response = requests.get("http://www.google.com", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[VALID] {proxy}{Style.RESET_ALL}")
            valid_proxies.append(proxy)
        else:
            print(f"{Fore.RED}[INVALID] {proxy}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}[INVALID] {proxy}{Style.RESET_ALL}")

def check_socks4_proxy(proxy):
    try:
        ip, port = proxy.split(":")
        socks.set_default_proxy(socks.SOCKS4, ip, int(port))
        socket.socket = socks.socksocket
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[VALID] {proxy}{Style.RESET_ALL}")
            valid_proxies.append(proxy)
        else:
            print(f"{Fore.RED}[INVALID] {proxy}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}[INVALID] {proxy}{Style.RESET_ALL}")

def check_socks5_proxy(proxy):
    try:
        ip, port = proxy.split(":")
        socks.set_default_proxy(socks.SOCKS5, ip, int(port))
        socket.socket = socks.socksocket
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[VALID] {proxy}{Style.RESET_ALL}")
            valid_proxies.append(proxy)
        else:
            print(f"{Fore.RED}[INVALID] {proxy}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}[INVALID] {proxy}{Style.RESET_ALL}")

def check_proxy_auth(proxy):
    try:
        ip, port, user, password = proxy.split(":")
        proxy_url = f"http://{user}:{password}@{ip}:{port}"
        response = requests.get("http://www.google.com", proxies={"http": proxy_url, "https": proxy_url}, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[VALID] {proxy}{Style.RESET_ALL}")
            valid_proxies.append(proxy)
        else:
            print(f"{Fore.RED}[INVALID] {proxy}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}[INVALID] {proxy}{Style.RESET_ALL}")

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    if mode == "1":
        executor.map(check_http_proxy, proxies)
    elif mode == "2":
        executor.map(check_socks4_proxy, proxies)
    elif mode == "3":
        executor.map(check_socks5_proxy, proxies)
    elif mode == "4":
        executor.map(check_proxy_auth, proxies)
    else:
        print(f"{Fore.RED}[!] Invalid!{Style.RESET_ALL}")
        exit()

if valid_proxies:
    with open("valid.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(valid_proxies) + "\n")

print(f"\n{Fore.GREEN}✅ Inspection complete!{Style.RESET_ALL}")
print(f"{Fore.CYAN}✔ Valid results are stored in: valid.txt{Style.RESET_ALL}")
