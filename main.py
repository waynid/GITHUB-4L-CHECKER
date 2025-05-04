import random
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

def g():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=4))

def c(u):
    r = requests.get(f"https://github.com/{u}")
    if r.status_code == 404 or BeautifulSoup(r.content, 'html.parser').find('img', alt="404"):
        response = requests.get(f"https://github.com/signup_check/username?value={u}")
        if "is available" in response.text:
            print(f"{Fore.GREEN}[ AVAILABLE ]{Style.RESET_ALL} {u}")
        elif "is not available" in response.text:
            print(f"{Fore.RED}[ TAKEN ]{Style.RESET_ALL} {u} (confirmed by API)")
        else:
            print(f"{Fore.YELLOW}[ UNKNOWN ]{Style.RESET_ALL} {u} (API inconclusive)")
    else:
        print(f"{Fore.RED}[ TAKEN ]{Style.RESET_ALL} {u}")

def m():
    [c(g()) for _ in range(9999)]

if __name__ == "__main__":
    m()
