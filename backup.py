import os
import pyautogui
from time import sleep
from colorama import Fore

os.system("clear")



username = "GC0156"
rep_name = input(Fore.GREEN + "[?] " + Fore.WHITE + "Repository Name: ")
rep_url = f"https://github.com/{username}/{rep_name}.git"
rep_local = f"C:/Users/Gui/Projects/{rep_name}"



file = open("commit_number.json", "r")
commit_number = int(file.readline(1))
origin = "origin"

os.system(f"cd {rep_local} && git init")
os.system(f"cd {rep_local} && git add *")
os.system(f'cd {rep_local} && git commit -m "commit {commit_number}"')
os.system(f"cd {rep_local} && git branch -M main")
os.system(f"cd {rep_local} && git remote add {origin} {rep_url}")
os.system(f"cd {rep_local} && git push -u {origin} main")

commit_value = commit_number + 1
commit_number2 = commit_value

file2 = open("commit_number.json", "w")
file2.truncate()
file2.write(str(commit_number2))



#os.system("clear")
#print(Fore.BLUE + "[!] " + Fore.WHITE + "Upload " + Fore.GREEN + "DONE" + Fore.WHITE + "!")
#sleep(2)
#os.system("clear")