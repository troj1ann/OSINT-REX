# username-checker.py
import json
from click import style
from numpy import block
import requests
from colorama import Fore, Style, init
import os
import time
from tqdm import tqdm
import pyfiglet
from termcolor import colored
import sys
from urllib.parse import urlparse


init(autoreset=True)

try:  # <<< Tüm scripti bu try bloğuna alıyoruz

    # ---------------------------------------------------------------------[DOWNLOADING]
    os.system("cls")
    for i in tqdm(range(50), desc=Fore.YELLOW + "Downloading" + Style.RESET_ALL, ncols=100, colour="white"):
        time.sleep(0.05)
    os.system("cls")

    # ---------------------------------------------------------------------[RENKLİ-BASLIK]
    ascii_art = pyfiglet.figlet_format("OSINT-REX", font="slant")

    colors = [
        "\033[38;2;255;255;0m",   # Sarı
        "\033[38;2;255;165;0m",   # Turuncu
        "\033[38;2;255;69;0m",    # Kırmızımsı turuncu
        "\033[38;2;255;20;147m",  # Sıcak pembe
        "\033[35m"                 # Açık pembe
    ]

    lines = ascii_art.split("\n")
    indent = 10  # sağa kaydırma miktarı (boşluk sayısı)

    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        print(color + (" " * indent) + line + "\033[0m")

    print(Fore.MAGENTA + "                           </> Author: Troj1ann | Pentester" + Style.RESET_ALL)
    print("                                                                         ")
    print(Fore.MAGENTA + "         ======================================================" + Style.RESET_ALL)
    print("                        " + Fore.MAGENTA + "Instagram" + Style.RESET_ALL + " @root_troj1ann")
    print(Fore.MAGENTA + "         ======================================================" + Style.RESET_ALL)
    print()  # boş satır

    # ---------------------------------------------------------------------[JSON'DAN SİTELERİ OKUMA]
    def load_sites():
        try:
            with open("sites.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("sites", [])
        except (FileNotFoundError, json.JSONDecodeError):
            print(Fore.RED + "[!] sites.json bulunamadi veya hatali. Varsayilan site listesi yüklendi." + Style.RESET_ALL)
            return [
                "https://github.com/{username}",
                "https://twitter.com/{username}",
                "https://www.instagram.com/{username}/",
                "https://www.reddit.com/user/{username}/",
                "https://www.pinterest.com/{username}/",
                "https://steamcommunity.com/id/{username}/"
            ]

    # ---------------------------------------------------------------------[KULLANICI ADI KONTROLÜ]
    def username_checker(username):
        if not username.strip():
            print(Fore.RED + "[!] Username boş olamaz!" + Style.RESET_ALL)
            return

        siteler = load_sites()  # JSON’dan liste çekiliyor
        print("\n")
        time.sleep(0.8)

        for site in siteler:
            site_filled = site.replace("{username}", username)
            site_name = urlparse(site_filled).netloc  # domain kısmı, örn: github.com
            try:
                cevap = requests.get(site_filled, timeout=5)
                if cevap.status_code == 200:
                    print(" " + Fore.YELLOW + "(" + Style.RESET_ALL + "OSINT-REX" + Fore.YELLOW + ")" +
                          Style.RESET_ALL + Fore.GREEN + f"[+] {site_filled}" + Style.RESET_ALL +
                          Fore.YELLOW + "--> " + Style.RESET_ALL + Fore.RED + "[" +
                          Style.RESET_ALL + "FOUND" + Fore.RED + "]" + Style.RESET_ALL +
                          " | " + Fore.CYAN + site_name + Style.RESET_ALL)
                elif cevap.status_code == 404:
                    print(" " + Fore.YELLOW + "(" + Style.RESET_ALL + "OSINT-REX" + Fore.YELLOW + ")" +
                          Style.RESET_ALL + Fore.RED + f"[-] {site_filled}" + Style.RESET_ALL +
                          Fore.YELLOW + "--> " + Style.RESET_ALL + Fore.RED + "[" +
                          Style.RESET_ALL + "NOT FOUND" + Fore.RED + "]" + Style.RESET_ALL +
                          " | " + Fore.CYAN + site_name + Style.RESET_ALL)
                else:
                    print(" " + Fore.YELLOW + "(" + Style.RESET_ALL + "OSINT-REX" + Fore.YELLOW + ")" +
                          Style.RESET_ALL + Fore.YELLOW + f"[?] {site_filled}" + Style.RESET_ALL +
                          Fore.YELLOW + "--> " + f"[Unknown Situation] ({cevap.status_code})" +
                          " | " + Fore.CYAN + site_name + Style.RESET_ALL)
            except requests.exceptions.RequestException:
                print(" " + Fore.YELLOW + "(" + Style.RESET_ALL + "OSINT-REX" + Style.RESET_ALL +
                      Fore.YELLOW + ")" + Style.RESET_ALL + Fore.RED + f"[!] {site_filled}" +
                      Style.RESET_ALL + Fore.YELLOW + "--> " + Style.RESET_ALL + Fore.RED +
                      "[" + Style.RESET_ALL + "Access Error" + Fore.RED + "]" + Style.RESET_ALL +
                      " | " + Fore.CYAN + site_name + Style.RESET_ALL)

    # ---------------------------------------------------------------------[TOOL MENÜSÜ]
    while True:
        print("")
        print("                         " + Fore.RED + "" + Style.RESET_ALL + Fore.RED + "⟬⟫┼ " + Style.RESET_ALL + Fore.MAGENTA +
              "USERNAME-CHECKER" + Style.RESET_ALL + Fore.RED + " ┼⟪⟭" + Style.RESET_ALL)
        print("                         " + Fore.RED + "" + Style.RESET_ALL + Fore.RED + "⟬⟫┼ " + Style.RESET_ALL + Fore.MAGENTA +
              "      Exit      " + Style.RESET_ALL + Fore.RED + " ┼⟪⟭" + Style.RESET_ALL)
        print("")

        try:
            secim = int(input(" " + Fore.YELLOW + "(" + Style.RESET_ALL + "OSINT-REX" + Style.RESET_ALL + Fore.YELLOW + ")" +
                              Style.RESET_ALL + Fore.MAGENTA + " 1 or 99 " + Style.RESET_ALL + Fore.RED + ">> " + Style.RESET_ALL))
        except ValueError:
            os.system("cls")
            print("Just Enter Numbers")
            continue

        if secim == 1:
            os.system("cls")
            print(" " + Fore.YELLOW + "(" + Style.RESET_ALL + "OSINT-REX" + Style.RESET_ALL + Fore.YELLOW + ")" + Style.RESET_ALL + Fore.BLUE + "Agent>" + Style.RESET_ALL + Fore.YELLOW + "Waiting")
            time.sleep(0.6)
            os.system("cls")
            time.sleep(0.5)
            print(" " + Fore.YELLOW + "(" + Style.RESET_ALL + "OSINT-REX" + Fore.YELLOW + ")" + Fore.BLUE + "Agent>" + Style.RESET_ALL + Fore.GREEN + "Running!")
            time.sleep(0.5)
            
            username = input(" " + Fore.YELLOW + "(" + Style.RESET_ALL + "OSINT-REX" + Style.RESET_ALL + Fore.YELLOW + ")" + Fore.BLUE + "UserName>" + Style.RESET_ALL)
            username_checker(username)
            print("\n\n")
            break

        elif secim == 99:
            print(Fore.RED + "Stopped by User" + Style.RESET_ALL)
            time.sleep(1)
            break

        else:
            print("Wrong Number")

except KeyboardInterrupt:
    # <<< Ctrl+C buradan yakalanacak
    print(Fore.RED + "Stopped by User" + Style.RESET_ALL )
    sys.exit(0)
