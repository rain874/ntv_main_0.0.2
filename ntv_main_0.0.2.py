#!/usr/bin/python3

import os.path
import requests
import hashlib
import random
import sys
import subprocess
from bs4 import BeautifulSoup
from randomUserAgent import randomUserAgent
from randomproxy import randomproxy

script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)
data = "/data/"
savefile = directory + data

open(savefile + "temp_link.txt", "w").close()
open(savefile + "temp_LinkHash.txt", "w").close()
open(savefile + "temp_headline.txt", "w").close()
open(savefile + "temp_date.txt", "w").close()
open(savefile + "temp_snippet.txt", "w").close()
open(savefile + "temp_rubID.txt", "w").close()

def ntv_de():

    proxylist = randomproxy.LoadProxyList()
    proxi = random.choice(proxylist)
    ipShuffle = (str(proxi))
    ipShuffle = ipShuffle.replace("'", "")
    ipShuffle2 = ipShuffle.replace("b", "")
    proxi = ipShuffle2

    proxies = {
          'http': proxi,
          'https': proxi,
    }
    uas = randomUserAgent.LoadUserAgents()
    ua = random.choice(uas)
    headers = {
         "Connection": "close",  # another way to cover tracks
         "User-Agent": ua
    }
    global url
    mainURL = "http://www.n-tv.de/"
    urlList = []
    urlList.append("politik")
    urlList.append("wirtschaft")
    urlList.append("sport")
    urlList.append("leute")
    urlList.append("technik")
    urlList.append("ratgeber")
    urlList.append("wissen")
    urlList.append("auto")
    urlList.append("reise")

    for i in range(0, 9):
        url = mainURL + urlList[i]

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')

        headlink = soup.find_all("article", {"class": "teaser teaser-680"})
        link = soup.find_all("article", {"class": "teaser teaser-220-450 clearfix"})

        def linkmake(l):
            for n in l:
                n = (n.a['href'])
                r = requests.get(n, headers=headers)
                rec = r.status_code
                if rec == 200:
                    f = open(savefile + "temp_link.txt","a")
                    f.write(n + "|" + '\n' )
                    r = requests.get(n, headers=headers)
                    soup = BeautifulSoup(r.text, 'lxml')
                    headline = soup.find("title")
                    for w in headline:
                        w = (w)
                        f = open(savefile + "temp_headline.txt", "a")
                        f.write(w + "|" + '\n')
                        f.close()
                    date_time = soup.find_all("meta", {"name": "date"})
                    for d in date_time:
                        d = (d['content'])
                        date = d[:-15]
                        time = d[-14:]
                        datetime = date + " " + time[:8]
                        f = open(savefile + "temp_date.txt", "a")
                        f.write(datetime + "|" + '\n')
                        f.close()
                    snippet = soup.find_all("meta", {"name": "description"})
                    for e in snippet:
                        e = (e['content'])
                        f = open(savefile + "temp_snippet.txt", "a")
                        f.write(e + "|" + '\n')
                        f.close()
                    f.close()
                    link_hash = hashlib.md5(str(n).encode('utf-8', 'ignore')).hexdigest()
                    f = open(savefile + "temp_LinkHash.txt", "a")
                    f.write(link_hash + "|" + '\n')
                    f.close()
                else:
                    print(rec)
                    #continue

        print("Crwal Headlines")
        linkmake(headlink)
        print("Crwal Links")
        linkmake(link)

def makefile():

    with open(savefile + "temp_link.txt", "r") as link:
        findLinks = link.readlines()

        searchObj_politik = "http://www.n-tv.de/politik/"
        searchObj_wirtschaft = "http://www.n-tv.de/wirtschaft/"
        searchObj_sport = "http://www.n-tv.de/sport/"
        searchObj_leute = "http://www.n-tv.de/leute/"
        searchObj_technik = "http://www.n-tv.de/technik"
        searchObj_ratgeber = "http://www.n-tv.de/ratgeber"
        searchObj_wissen = "http://www.n-tv.de/wissen"
        searchObj_auto = "http://www.n-tv.de/auto"
        searchObj_reise = "http://www.n-tv.de/reise"

        for i in findLinks:
            if searchObj_politik in i:
                f = open(savefile + "temp_rubID.txt", "a")
                f.write("21" + '\n')
                f.close()
            elif searchObj_wirtschaft in i:
                f = open(savefile + "temp_rubID.txt", "a")
                f.write("9" + '\n')
                f.close()
            elif searchObj_sport in i:
                f = open(savefile + "temp_rubID.txt", "a")
                f.write("16" + '\n')
                f.close()
            elif searchObj_leute in i:
                f = open(savefile + "temp_rubID.txt", "a")
                f.write("14" + '\n')
                f.close()
            elif searchObj_technik in i:
                f = open(savefile + "temp_rubID.txt", "a")
                f.write("12" + '\n')
                f.close()
            elif searchObj_ratgeber in i:
                f = open(savefile + "temp_rubID.txt", "a")
                f.write("13" + '\n')
                f.close()
            elif searchObj_wissen in i:
                f = open(savefile + "temp_rubID.txt", "a")
                f.write("10" + '\n')
                f.close()
            elif searchObj_auto in i:
                f = open(savefile + "temp_rubID.txt", "a")
                f.write("15" + '\n')
                f.close()
            elif searchObj_reise in i:
                f = open(savefile + "temp_rubID.txt", "a")
                f.write("11" + '\n')
                f.close()
            else:
                f = open(savefile + "temp_rubID.txt", "a")
                f.write("19" + '\n')
                f.close()

    global data
    with open(savefile + "temp_link.txt") as temp_link, \
         open(savefile + "temp_LinkHash.txt") as temp_hash, \
         open(savefile + "temp_headline.txt") as temp_headline, \
         open(savefile + "temp_snippet.txt") as temp_snippit, \
         open(savefile + "temp_rubID.txt") as temp_rubID, \
         open(savefile + "temp_date.txt") as temp_date:
         text1 = temp_link.read().splitlines()
         text2 = temp_hash.read().splitlines()
         text3 = temp_headline.read().splitlines()
         text4 = temp_snippit.read().splitlines()
         text5 = temp_date.read().splitlines()
         text6 = temp_rubID.read().splitlines()

         linkmax = len(text1)
         line_c_hash = len(text2)
         line_c_headline = len(text3)
         line_c_snippit = len(text4)
         line_c_date = len(text5)
         line_c_rubID = len(text6)

    if linkmax == line_c_hash and linkmax == line_c_headline and linkmax == line_c_snippit and linkmax == line_c_date and linkmax == line_c_rubID:
        print("Starte next Script")
        process = subprocess.Popen(["bash", "ntv_paste_temp_crwaler_txt.sh"])
        print("Beende ntv_main")
        exit()
    else:
        print("line Error.")

print("Starte Crwaler für n-tv.de")
ntv_de()
print("Speicher Daten für n-tv.de")
makefile()


# Alter der proxylister DATEI ermitteln
'''
fileDate = subprocess.check_output(["date", "-r", "out_filtered.txt", "+%R"])
currentDate = subprocess.check_output(["date", "+%R"])
# ProxieDatei erneuern bei einer Zeitdifferrenz berechnen kleiner als 1 Tag

fileTime = subprocess.check_output(["date", "-r", "out_filtered.txt", "+%R"])
currentTime = subprocess.check_output(["date", "+%R"])
# ProxieDatei erneuern bei einer Zeitdifferrenz berechnen kleiner als 180 min

script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)
proxfile="/random_proxy/python-proxy-checker/output/out_filtered.txt"
# date

credate = time.strftime('%d%m%Y', time.gmtime(os.path.getmtime(directory + proxfile)))
curdate = (datetime.datetime.now().strftime('%d%m%Y'))

# time

creattime = time.strftime('%H', time.ctime(os.path.getctime(directory + proxfile)))
curdate = datetime.datetime.now()
print(creattime)
print(creattime)

curtime = datetime.datetime.now().strftime("%H")
print(curtime)

curtimeINT = (int(curtime))
cretimeINT = (int(creattime))

timedifferenz =  curtimeINT - cretimeINT

print(timedifferenz)

# date and time visible check
if credate == curdate and timedifferenz >= 2:
    print("Die Proxie list ist aktuell, crwaler wird gestartet")
else:
    print("Proxielist zu alt proxycheck wird gestartet") '''
