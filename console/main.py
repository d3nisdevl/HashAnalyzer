from colorama import Fore, init
import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from config import HASH_TYPES   # <--> Импортируем словарик с хешами <3


init(autoreset=True)


Success = Fore.GREEN + "[+]" + Fore.RESET
Error = Fore.RED + "[-]" + Fore.RESET
Info = Fore.BLUE + "[*]" + Fore.RESET


class HashDetector:
    def __init__(self) -> None:
        self.hash_types = HASH_TYPES


    def detect(self, hash_str) -> dict:
        if not hash_str:
            return {'type': 'UNKNOWN', 'desc': 'Unknown hash', 'length': 0, 'hashcat': 'UNKNOWN'}
        
        hash_str = hash_str.strip().lower()
        length = len(hash_str)
        
        for name, props in self.hash_types.items():
            if length == props['length'] and re.match(props['pattern'], hash_str):
                return {'type': name, 'desc': props['desc'], 'length': length, 'hashcat': props['hashcat']}
        
        return {'type': 'UNKNOWN', 'desc': 'Unknown hash', 'length': length, 'hashcat': 'UNKNOWN'}


def show_banner() -> str:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + """
    █████   █████                   █████        █████████              ████                               
    ░░███   ░░███                   ░░███        ███░░░░░███            ░░███                               
    ░███    ░███   ██████    █████  ░███████   ░███    ░███  ████████   ░███  █████ ████  █████████  █████ 
    ░███████████  ░░░░░███  ███░░   ░███░░███  ░███████████ ░░███░░███  ░███ ░░███ ░███  ░█░░░░███  ███░░  
    ░███░░░░░███   ███████ ░░█████  ░███ ░███  ░███░░░░░███  ░███ ░███  ░███  ░███ ░███  ░   ███░  ░░█████ 
    ░███    ░███  ███░░███  ░░░░███ ░███ ░███  ░███    ░███  ░███ ░███  ░███  ░███ ░███    ███░   █ ░░░░███
    █████   █████░░████████ ██████  ████ █████ █████   █████ ████ █████ █████ ░░███████   █████████ ██████ 
    ░░░░░   ░░░░░  ░░░░░░░░ ░░░░░░  ░░░░ ░░░░░ ░░░░░   ░░░░░ ░░░░ ░░░░░ ░░░░░   ░░░░░███  ░░░░░░░░░ ░░░░░░  
                                                                                ███ ░███                    
                                                                                ░░██████                     
                                                                                ░░░░░░                      
                                        [https://github.com/d3nisdevl]
        """)
    
    print(Fore.YELLOW + "Hash Analyzer v1.0" + Fore.RESET)
    print(Fore.YELLOW + "<---------------->" + Fore.RESET)


def hash_analyzer() -> str:
    show_banner()

    detector = HashDetector()
    
    while True:
        user_input = input(Info + Fore.WHITE + f" Enter Hash (or {Fore.RED}'quit'{Fore.RESET}): " + Fore.RESET).strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            break

        elif user_input.lower() == 'clear':
            hash_analyzer()

        if not user_input:
            continue
            
        result = detector.detect(user_input)
        
        print('\n' + Fore.WHITE + Success + f" Type - {Fore.YELLOW} {result['type']} {Fore.RESET}" + Fore.RESET)
        print(Fore.WHITE + Success + f" Desc - {Fore.YELLOW} {result['desc']} {Fore.RESET}" + Fore.RESET)
        print(Fore.WHITE + Success + f" Length - {Fore.YELLOW} {result['length']} {Fore.RESET}" + Fore.RESET)
        print(Fore.WHITE + Success + f" Hashcat - {Fore.YELLOW} {result['hashcat']} {Fore.RESET}\n" + Fore.RESET)

        print(Fore.YELLOW + "##################" + Fore.RESET)


def main() -> None:
    hash_analyzer()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + '\n\n<- Goodbye!.. ->' + Fore.RESET)