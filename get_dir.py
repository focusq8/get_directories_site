import requests
from os import system

Red = "\033[1;31;40m"
Blue = "\033[1;36;40m"
Yellow="\033[0;33m"

try:
    with open("wordlist.txt", 'r') as lists:
        wordslist = lists.read().splitlines()
except FileNotFoundError:
    input("Couldn't find wordlist.txt!")

url =  input("Enter Your Site: ")
system('cls||clear')

if 'https://' in url:
  url
else:
  url = 'http://'+url

for lists in wordslist:
        add = url+"/"+lists
        try:
            geturl = requests.get(add)
            if "Page Not Found" in geturl.text:
                print(f"{Red}page not found {add}")
                with open("found.txt", 'a') as file:
                    file.write(f"Page Not Found {add}\n")
                    continue

            elif geturl.status_code == 200:
                print(f"{Blue}Found {add}")
                with open("found.txt", 'a') as file:
                    file.write(f"Found {add}\n")
                    continue

            elif geturl.status_code == 403:
                print(f"{Yellow}Forbidden {add}")
                with open("Forbidden.txt", 'a') as file:
                    file.write(f"Forbidden {add}\n")
                    continue            
            else:
                print(f"{Red}Not Found {add}")
                
        except:
            print(f"{Red} Error: {geturl.status_code} {add}\n")
input("Finished !!!")
