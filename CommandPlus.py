import os
import webbrowser as wb
import json
from linkssaver import *
import time as t
print("Welcome to CommandPlus Application")
def MainOfApp():
    print("")
    print("")
    print("Type help to see All Commands Available :)")
    print()
    print()
    while True:
        user = input("Type Command: ")
        if user == "help":
            helplist = ["1)Maths Collections", "2)Games Downloader", "3)Apps Downloader", "4)Easy Web"]
            for hlist in helplist:
                print(hlist)
        elif user == "1":
            print("")
            print("")
            print("------------------")
            print("")
            print("Open Maths Collection...")
            print("")
            print("------------------")
            print("")
            print("")
            Calculator()
            break
        elif user == "cpver":
            print("-----------------------------")
            print("")
            print("CommandPlus 1.3.b19")
            print("")
            print("-----------------------------")
            print("")
            print("This Application By GigaCoder")
            print("")
            print("-----------------------------")
            wb.open('https://www.youtube.com/channel/UCU-JNUKw9HRkkjSKRjud5qw')
            
        elif user == "3":
            print("")
            print("")
            print("------------------")
            print("")
            print("Open Apps Downloader...")
            print("")
            print("------------------")
            print("")
            print("")
            Apps_Downloader()
            break
        elif user == "2":
            print("")
            print("")
            print("------------------")
            print("")
            print("Open Games Downloader...")
            print("")
            print("------------------")
            print("")
            print("")
            Games_Downloader()
            break
        elif user == "4":
            print("")
            print("")
            print("------------------")
            print("")
            print("Open Easy Web...")
            print("")
            print("------------------")
            print("")
            print("")
            webbrowsing()
            break
        else:
            print("Invalid Command")
def Calculator():
    while True:
        user = input("Type Command: ")
        if user == "help":
            helplist = ["1)Back", "2)Basic Calculator", "3)Convertor", "4)Numbers Sorter"]
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
            elif operator == "^":
                print(num1, "^", num2, "=", num1 ** num2)
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
            unitslists = ["1)km -> m", "2)m -> km", "3)s -> min", "4)min -> s", "5)s -> h", "6)h -> s", "7)mile -> km", "8)km -> mile"]
            print()
            print()
            for i in unitslists:
                print(i)
            print()
            print()
            while True:
                you = input("Select: ")
                if you == "1":
                    km0 = float(input("km: "))
                    m0 = km0 * 1000
                    print("")
                    print("kilometers to meters:" ,m0)
                elif you == "2":
                    m = float(input("m: "))
                    km = m / 1000
                    print("")
                    print("meters to kilometers:", km)
                elif you == "3":
                    s = float(input("seconds: "))
                    min = s / 60
                    print("")
                    print("seconds to minutes:", min)
                elif you == "4":
                       min0 = float(input("minutes: "))
                       s0 = min0 * 60
                       print()
                       print("minutes to seconds:", s0)
                elif you == "5":
                    s1 = float(input("seconds: "))
                    h = s1 / 3600
                    print()
                    print("seconds to hours:",h)

                elif you == "6":
                    h0 = float(input("hours: "))
                    s2 = h0 * 3600
                    print()
                    print("hours to seconds:", s2)
                elif you == "7":
                    miles = float(input("miles: "))
                    km1 = miles * 1.609344
                    print()
                    print("miles to kilometers:" ,km1)
                elif you == "8":
                    km2 = float(input("km: "))
                    miles0 = km2 / 1.609344
                    print()
                    print("kilometers to miles: ", miles0)
                elif you == "back":
                    MainOfApp()
                    print("--------------------------")
                    print("")
                    print("Retune To The Main Menu...")
                    print("")
                    print("--------------------------")
                    break
        
        elif user == "4":
            helplistt = ["1)Very Basic Numbers Sorter", "2)NumbersSorter with Calculator"]
            print()
            print()
            for i in helplistt:
                print(i)
            print()
            print()
            while True:
                you = input("Select: ")
                if "1" in you:
                    mylist = []
                    hmn = int(input("How many Numbers: "))
                    if hmn > 5:
                        print()
                        print()
                        print("Error: The Maximum Value is 5")
                        print()
                        print()
                        break
                    elif hmn < 2:
                        print()
                        print()
                        print("Error: Minimum Value is 2")
                        print()
                        print()
                        break
                    nosame = 0
                    for i in range(hmn):
                        nosame += 1
                        num = input("number " + str(nosame) + ": ")
                        mylist.append(num)
                    mylist.sort(reverse=True)
                    for i in mylist:
                        print(i)
                    mylist.clear()
                elif "2" in you:
                    listofwqulisation = []
                    while True:
                        print()
                        print()
                        print("Command Availabel:")
                        print()
                        print()
                        print("back: And this command Type it after the answer shows")
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
                            listofwqulisation.append(num1 + num2)
                        elif operator == "-":
                            print(num1, "-", num2, "=", num1 - num2)
                            listofwqulisation.append(num1 - num2)
                        elif operator == "*":
                            print(num1, "*", num2, "=", num1 * num2)
                            listofwqulisation.append(num1 * num2)
                        elif operator == "/":
                            print(num1, "/", num2, "=", num1 / num2)
                            listofwqulisation.append(num1 / num2)
                        elif operator == "^":
                            print(num1, "^", num2, "=", num1 ** num2)
                            listofwqulisation.append(num1 ** num2)
                        else:
                            print("Invalid Operator", ">>>", operator)
                        useryou = input("Do you Wanna to sort it(yes or no): ")
                        if useryou == "no":
                            pass
                        elif useryou == "yes":
                            if len(listofwqulisation)>=2:

                                listofwqulisation.sort(reverse=True)
                                print()
                                for i in listofwqulisation:
                                    print(i)
                                listofwqulisation.clear()
                            else:
                                print("Error")
                        elif useryou == "back":
                            break
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
            plist = ["1)Audacity", "2)Git", "3)Aseprite", "4)Krita", "5)VLC", "6)Bandicam(Trial)", "7)Blender(2.8)", "8)K-Lite Codec Pack(Mega)", "9)Discord"]
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
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\GitSetup.exe')
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
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\AsepriteSetup.exe')
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
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\KritaSetup.exe')
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
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\VLC_Setup.exe')
                
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
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\BandicamSetup.exe')
                
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
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\BlenderSetup.exe')
                
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif userinstall == "8":
                print("----------------------")
                print("")
                print("Installing K-Lite CodecPack(Mega)...")
                print("")
                print("----------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\KLiteMega.exe')
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            elif userinstall == "9":
                print("----------------------")
                print("")
                print("Installing Discord...")
                print("")
                print("----------------------")
                os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\T&P\DiscordSetup.exe')
                
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
            elif userinstall == "back":
                break
            else:
                print("Error(Programme Not Found)")
        elif user == "back":
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        else:
            print("Invalid Command")
#Updated
def Games_Downloader():
    while True:
        user = input("Type_Command: ")
        helplist = ["1)GeometryDash(Crack)","2)Opticraft","3)TLauncher"]
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
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif user == "2":
            print("-------------------------")
            print("")
            print("Downloading Opticraft")
            print("")
            print("-------------------------")
            os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\Browsers\OC_Setup.exe')
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif user == "3":
            print("-------------------------")
            print("")
            print("Downloading TLauncher")
            print("")
            print("-------------------------")
            os.startfile('C:\Program Files (x86)\CommandPlus\Datas.CdP\AppsInstall\Browsers\TLauncherSetup.exe')
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break

        elif user == "back":
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        else:
            print("Game Not Found")
#Updated
def webbrowsing():
    helplist = ["yt: Youtube", "fb:Facebook", "twi: Twitter", "gg: Google", "ig: Instagram", "crt-fav: create favorites", "r: remove favorite"]
    helpfav = []
    while True:
        user = str(input("Type_Command: "))
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
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif user == "fb":
            wb.open('https://facebook.com')
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif user == "twi":
            wb.open('https://twitter.com')
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif user == "gg":
            wb.open('https://google.com')
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif user == "ig":
            wb.open('https://instagram.com')
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif user == "back":
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif user == "crt-fav":
            if len(helpfav) == 5:
                print()
                print("You reached The Maximum Value")
                print()
            else:
                hmws = int(input("How much web sites(MAXIMUM 5): "))
                if hmws > 5:
                    print("ERROR!!")
                    print()
                    print("The Maximum Value is 5")
                    print()
                    print("--------------------------")
                    print("")
                    print("Retune To The Main Menu...")
                    print("")
                    print("--------------------------")
                    MainOfApp()
                    break
                linkint = 0
                scint = 0
                vint = 0
                nint = 0
                with open('linkssaver.py', "w") as f:
                    for i in range(hmws):
                        linkint += 1
                        Link = input("Link" + str(linkint) + ": ")
                        scint += 1
                        Shortcut = input("Shortcut" + str(scint) + ": ")
                        nint += 1
                        Name = input("Name" + str(nint) + ": ")
                        vint += 1
                        f.write("Link" + str(vint) + " = " + "'https://" + Link + "'" + "\n")
                        f.write("sc" + str(vint) + " = " + '"' + Shortcut + '"' + "\n")
                        helpfav.append(Shortcut + ": " + Name)
                        print("You created The favorites succesfully (:")
                        print()
                        print()
                with open('userfav.json', "w") as fjson:
                    json.dump(helpfav, fjson, indent=4)
                print("Restart to Apply Changes After...")
                t.sleep(1.25)
                print("1"+"...")
                t.sleep(1.25)
                print("2"+"...")
                t.sleep(1.25)
                print("3"+"...")
                t.sleep(2)
                os.startfile('C:\Program Files (x86)\CommandPlus\CommandPlus.exe')
                exit()

        elif user == "r":
            helpfav.clear()
            with open('userfav.json', "w") as f:
                json.dump(helpfav, f, indent=4)
            with open('linkssaver.py', "w") as f:
                    f.write("#NONE")
            print("All The Favorits are succesfully Cleared (:")
            print()
            print()
        elif user == "helpf":
            with open('userfav.json') as file:
                helpfav = json.load(file)
            if len(helpfav) == 0:
                print()
                print()
                print("--------You Don't Have any Favorites-------")
                print("-------------------------------------------")
                print("Type The Command crt-fav to Create Favorits")
                print("-------------------------------------------")
                print()
                print()
            else:

                print("")
                print()
                for i in helpfav:
                    print(i)
                print("")
                print()
        elif sc1 in user:
            wb.open(Link1)
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif sc2 in user:
            wb.open(Link2)
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif sc3 in user:
            wb.open(Link3)
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif sc4 in user:
            wb.open(Link4)
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        elif sc5 in user:
            wb.open(Link5)
            print("")
            print("")
            print("Wait for Seconds...")
            print()
            print()
            MainOfApp()
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            break
        else:
            print("Error Command Not Found")
MainOfApp()
