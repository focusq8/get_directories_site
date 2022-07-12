import requests
from os import system

Red = "\033[1;31;40m"
Blue = "\033[1;36;40m"
green = '\033[1;32;40m'
Yellow="\033[0;33m"
White="\033[0;37m"

def get_dir():
        
    system(f"title Basic Tool To Get Directories Site")
    system('cls||clear')
    host = input(f"""{green}
For example: http://testphp.vulnweb.com



Enter your url please: """)

    file = input("\nEnter your file please: ")
    with open(file, 'r') as lists:
        wordslist = lists.read().splitlines()

    system('cls||clear')
    try:
        for words in wordslist:
            url =f"{host}/{words}"
            req = requests.get(url)

            if req.status_code == 200:
                print(f"{Blue} Found: {url}\n")
            
            elif req.status_code == 404:
                print(f"{Red} Not Found: {url}\n")
            else:
                print(f"{Yellow} Error: {req.status_code} {url}\n")

        input(f"{White}\n\n\nFinished......")
    except:
        print("exit")
        exit()
    
def sub_dir():

    system(f"title Basic Tool To Get Directories Site")
    system('cls||clear')
    host = input(f"""{green}
For example: vulnweb.com



Enter your url please: """)

    file = input("\nEnter your file please: ")
    with open(file, 'r') as lists:
        wordslist = lists.read().splitlines()

    system('cls||clear')
    try:
        for words in wordslist:
            url ="http://"+words+"."+host
            
            try:
                req = requests.get(url)

                if req.status_code == 200:
                    print(f"{Blue} Found: {url}\n")
                
                elif req.status_code == 400:
                    print(f"{Red} Not Found: {url}\n")
                else:
                    print(f"{Yellow} Error: {req.status_code} {url}\n")
            except requests.ConnectionError:
                pass

        input(f"{White}\n\n\nFinished......")
    except:
        print("exit")
        exit()

sub_dir()