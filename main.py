import random, requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

def g(): return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=3))

def c(u):
    r = requests.get(f"https://github.com/{u}")
    if r.status_code == 404 or BeautifulSoup(r.content, 'html.parser').find('img', alt="404"):
        print(f"{Fore.GREEN}[ AVAILABLE ]{Style.RESET_ALL} {u}")
    else:
        print(f"{Fore.RED}[ TAKEN ]{Style.RESET_ALL} {u}")

def m(): [c(g()) for _ in range(9999)]

if __name__ == "__main__": m()
