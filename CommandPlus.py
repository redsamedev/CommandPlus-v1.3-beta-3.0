import os
import webbrowser as wb
import json
from linkssaver import *
print("Welcome to CommandPlus Application")
def MainOfApp():
    print("")
    print("")
    print("Type help to see All Commands Available :)")
    print()
    print()
    print()
    while True:
        user = input("Type Command: ")
        if user == "help":
            helplist = ["1)Calculator", "2)Games Downloader", "3)Apps Downloader", "4)Web Shortcuts"]
            for hlist in helplist:
                print(hlist)
        elif user == "1":
            print("")
            print("")
            print("------------------")
            print("")
            print("Open Calculator...")
            print("")
            print("------------------")
            print("")
            print("")
            Calculator()
            break
        elif user == "cpver":
            print("-----------------------------")
            print("")
            print("CommandPlus 1.3")
            print("")
            print("-----------------------------")
            print("")
            print("This Application By GigaCoder")
            print("")
            print("-----------------------------")
            wb.open('https://www.youtube.com/channel/UCU-JNUKw9HRkkjSKRjud5qw')
            
        elif user == "3":
            print("Opening Apps Downloader...")
            print("")
            Apps_Downloader()
            break
        elif user == "2":
            print("Opening GamesDownloader...")
            print("")
            Games_Downloader()
            break
        elif user == "4":
            print("opening Web Shortcuts...")
            print("")
            webbrowsing()
            break
        else:
            print("Invalid Command")
def Calculator():
    while True:
        user = input("Type Command: ")
        if user == "help":
            helplist = ["1)Back", "2)Basic Calculator", "3)Convertor"]
            for i in helplist:
                print(i)
        elif user == "2":
            print("")
            print("")
            num1 = float(input("First Number: "))
            print("")
            operator = str(input("Operator: "))
            print("")
            num2 = float(input("Second Number: "))
            #System
            if operator == "+":
                print(num1, "+", num2, "=", num1 + num2)
            elif operator == "-":
                print(num1, "-", num2, "=", num1 - num2)
            elif operator == "*":
                print(num1, "*", num2, "=", num1 * num2)
            elif operator == "/":
                print(num1, "/", num2, "=", num1 / num2)
            elif operator == "**":
                print(num1, "**", num2, "=", num1 ** num2)
            else:
                print("Invalid Operator", ">>>", operator)
        elif user == "1":
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            
            MainOfApp()
            break
        elif user == "3":
            unitslists = ["1)km -> m", "2)m -> km", "3)s -> min", "4)min -> s"]
            while True:
                you = input("Type_Help: ")
                if you == "help":
                    for i in unitslists:
                        print(i)
                elif you == "1":
                    km0 = float(input("km: "))
                    m0 = km0 * 1000
                    print("")
                    print("Kilometers to meters =" ,m0)
                elif you == "2":
                    m = float(input("m: "))
                    km = m / 1000
                    print("")
                    print("Kilometers to meters =", km)
                elif you == "3":
                    s = float(input("seconds: "))
                    min = s / 60
                    print("")
                    print("seconds to minutes =", min)
                elif you == "4":
                       min0 = float(input("minutes: "))
                       s0 = min0 * 60
                       print()
                       print("minutes to seconds =", s0)
        else:
            print("Invalid Command")
def Apps_Downloader():
    while True:
        user = input("Type Command: ")
        if user == "help":
            listh = ["1)Browsers","2)Programmes"]
            for i in listh:
                print(i)
        elif user == "1":
            print("All Browsers Available:")
            print("")
            print("")
            print("1)Google Chrome")
            print("2)Mozilla FireFox")
            print("3)Brave")
            print("4)Microsoft Edge")
            print("")
            print("")
            installuser = input("Select The Browser: ")
            if installuser == "1":
                print("---------------------------")
                print("")
                print("Installing Google Chrome...")
                print("")
                print("---------------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\Browsers\ChromeSetup.exe')
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif installuser == "2":
                print("-----------------------------")
                print("")
                print("Installing Mozilla FireFox...")
                print("")
                print("-----------------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\Browsers\Firefox_Setup.exe')
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif installuser == "3":
                print("-------------------")
                print("")
                print("Installing Brave...")
                print("")
                print("-------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\Browsers\BraveSetup.exe')
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif installuser == "4":
                print("----------------------------")
                print("")
                print("Installing Microsoft Edge...")
                print("")
                print("----------------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\Browsers\MicrosoftEdgeSetup.exe')
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            else:
                print("Error(Programme Not Found)")
        elif user == "2":
            plist = ["1)Audacity", "2)Git", "3)Aseprite", "4)Krita", "5)VLC", "6)Bandicam(Trial)", "7)Blender(2.8)"]
            print("")
            print("")
            for i in plist:
                print(i)
            print("")
            print("")
            userinstall = input("Select Programme: ")
            if userinstall == "1":
                print("----------------------")
                print("")
                print("Installing Audacity...")
                print("")
                print("----------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\AudacitySetup.exe')
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif userinstall == "2":
                print("----------------------")
                print("")
                print("Installing Git...")
                print("")
                print("----------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\GitSetup')
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif userinstall == "3":
                print("----------------------")
                print("")
                print("Installing Aseprite...")
                print("")
                print("----------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\AsepriteSetup')
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif userinstall == "4":
                print("----------------------")
                print("")
                print("Installing Krita...")
                print("")
                print("----------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\KritaSetup')
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif userinstall == "5":
                print("----------------------")
                print("")
                print("Installing VLC_Setup...")
                print("")
                print("----------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\VLC_Setup')
                
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif userinstall == "6":
                print("----------------------")
                print("")
                print("Installing Bandicam...")
                print("")
                print("----------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\BandicamSetup')
                
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif userinstall == "7":
                print("----------------------")
                print("")
                print("Installing Blender(2.8)...")
                print("")
                print("----------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\BlenderSetup')
                
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif userinstall == "back":
                break
            else:
                print("Error(Programme Not Found)")
        elif user == "back":
            MainOfApp()
            break
        else:
            print("Invalid Command")
#Updated
def Games_Downloader():
    while True:
        user = input("Type_Command: ")
        helplist = ["1)GeometryDash(Crack)","2)Opticraft"]
        if user == "help":
            for i in helplist:
                print(i)
        elif user == "1":
            print("-------------------------")
            print("")
            print("Downloading Geometry Dash")
            print("")
            print("-------------------------")
            os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\Browsers\GeometryDash.exe')
            MainOfApp()
            break
        elif user == "2":
            print("-------------------------")
            print("")
            print("Downloading Opticraft")
            print("")
            print("-------------------------")
            os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\Browsers\OC_Setup')
            MainOfApp()
            break
        elif user == "back":
            MainOfApp()
            break
        else:
            print("Game Not Found")
#Updated
def webbrowsing():
    helplist = ["yt: Youtube", "fb:Facebook", "twi: Twitter", "gg: Google", "ig: Instagram", "crt-fav: create favorites", "r: remove favorite"]
    with open('userdatas.json') as f:
        helplist = json.load(f)
    while True:
        using = 5
        user = input("Type_Command: ")
        if user == "help":
            print("")
            print("")
            for i in helplist:
                print(i)
            print("")
            print("")
        elif user == "yt":
            wb.open('https://youtube.com')
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            break
        elif user == "fb":
            wb.open('https://facebook.com')
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            break
        elif user == "twi":
            wb.open('https://twitter.com')
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            break
        elif user == "gg":
            wb.open('https://google.com')
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            break
        elif user == "ig":
            wb.open('https://instagram.com')
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            break
        elif user == "back":
            MainOfApp()
            break
        elif user == "crt-fav":
            hmws = int(input("How much web sites(MAXIMUM 5): "))
            using -= hmws
            linkint = 0
            scint = 0
            vint = 0
            nint = 0
            with open('linkssaver.py', "w") as f, open('userdatas.json', "w") as fjson:
                for i in range(hmws):
                    linkint += 1
                    Link = input("Link" + str(linkint) + ": ")
                    scint += 1
                    Shortcut = input("Shortcut" + str(scint) + ": ")
                    nint += 1
                    Name = input("Name" + str(nint) + ": ")
                    vint += 1
                    f.write("Link" + str(vint) + " = " + "'https://" + Link + "'" + "\n")
                    f.write("sc" + str(vint) + " = " + "'" + Shortcut + "'" + "\n")
                    helplist.append(Shortcut + ": " + Name)
                f.write("using0 = " + str(using) + "\n")
                json.dump(helplist, fjson, indent=4)
            if hmws > 5:
                print("ERROR!!")
        elif user == "r":
            for i in helplist:
                print(i)
            print("")
            print()
            print()
            remover = int(input("What do You want to remove: "))
            del helplist[remover]
            with open('userdatas.json', "w") as f:
                json.dump(helplist, f, indent=4)
            with open('linkssaver.py', "w") as f:
                    f.write("#NONE")
        elif user == "crt-fav" and using0 == 0:
            print("Error")
        elif user == sc1:
            wb.open(Link1)
            break
        elif user == sc2:
            wb.open(Link2)
        elif user == sc3:
            wb.open(Link3)
        elif user == sc4:
            wb.open(Link4)
        elif user == sc5:
            wb.open(Link5)
        else:
            print("Error Command Not Found")

MainOfApp()
