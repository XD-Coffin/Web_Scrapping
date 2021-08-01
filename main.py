import argparse
import os
import requests
from bs4 import BeautifulSoup
import termcolor
import gtts
import sys
from voice import vocals
from playsound import playsound

parser = argparse.ArgumentParser(description="Web-scrapping with python...")
parser.add_argument("-m", "--mode", type=str, metavar="", required=True, help="normal/voice modes are availiable")
args = parser.parse_args()

def art():
    while True:
        print( """
        _________                          .__  __           
        /   _____/ ____   ____  __ _________|__|/  |_ ___.__. 
        \_____  \_/ __ \_/ ___\|  |  \_  __ \  \   __<   |  | 
        /        \  ___/\  \___|  |  /|  | \/  ||  |  \___  | 
        /_______  /\___  >\___  >____/ |__|  |__||__|  / ____| 
                \/     \/     \/                       \/      
            __________.__                                      
            \______   \  |   ____   ____  ______               
            |    |  _/  |  /  _ \ / ___\/  ___/               
            |    |   \  |_(  <_> ) /_/  >___ \                
            |______  /____/\____/\___  /____  >  /\   /\   /\ 
                   \/           /_____/     \/   \/   \/   \/ 

                       
            WEB-SCRAPING WITH PYTHON:

                        1. The Hacker News.
                        2. Security Week.
                        3. Security Weekly.
                        4. Cyber-Daily.
                                                Type "exit" to exit the program.
                                                os commands are also supported.
                                                Coded by Sahil Singh.
        """)
        ask = str(input(termcolor.colored("Choose the blog: ", "red")))
        if ask == "1":
            num = 1
            url = "https://thehackernews.com/"   
            a = requests.get(url)
            content = a.content
            soup = BeautifulSoup(content, 'html.parser')
            hyperlinks = BeautifulSoup(content, 'html.parser')
            while (num < 6):
                headlines = soup.find_all('h2', class_="home-title").__getitem__(num)
                hyperlinks = soup.find_all("a", class_="story-link").__getitem__(num)
                print(f"{num}) {headlines.get_text()}")
                print(hyperlinks.get_text())
                print("")
                num+=1
                input("Press any key to continue: ")
            os.system("clear")

        elif ask == "2":
            url = "https://www.securityweek.com/"
            num = 1
            a = requests.get(url) 
            content = a.content
            soup = BeautifulSoup(content, 'html.parser')
            while num < 6:
                headlines = soup.find_all("span", class_="field-content").__getitem__(num)
                print(f"{num}) {headlines.get_text()}")
                num+=1
            input("Press any key to continue: ")
            os.system("clear")

        elif ask == "3":
            url = "https://securityweekly.com/blog"
            a = requests.get(url) 
            num = 1
            content = a.content
            soup = BeautifulSoup(content, 'html.parser')
            while num < 4:
                headlines = soup.find_all("h2", class_="fl-post-title").__getitem__(num)
                long = soup.find_all("div", class_="fl-post-excerpt").__getitem__(num)
                print(f"{num}) {headlines.get_text()}")
                
        elif ask == "4":
            url = "https://cyberdaily.securelayer7.net/"
            a = requests.get(url)
            num = 1 
            content = a.content
            soup = BeautifulSoup(content, 'html.parser')
            while num < 3:
                headlines = soup.find_all("div", class_="featuredBlock--altGrid--minor-item col-xs-12 col-md-4").__getitem__(num)
                print(f"{num}) {headlines.get_text()}")
                num+=1
            input("Press any key to continue: ")
            os.system("clear")

        elif ask == "exit":
            sys.exit()
        
        else:
            os.system(ask)

if args.mode == "normal":
    art()       

elif args.mode == "voice":
    vocals()
