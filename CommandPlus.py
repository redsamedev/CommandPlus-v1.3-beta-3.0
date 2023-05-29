import os
import webbrowser as wb
print("Welcome to CommandPlus Application")
def MainOfApp():
    print("")
    print("")
    print("Type help to see All Commands Available :)")
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
            print("CommandPlus 1.2")
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
            helplist = ["1)Back", "2)Start The Calculator"]
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
        else:
            print("Invalid Command")
def Apps_Downloader():
    while True:
        user = input("Type Command: ")
        if user == "help":
            listh = ["1)Browsers","Programmes"]
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
            else:
                print("Error(Programme Not Found)")
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
        else:
            print("Game Not Found")
#Updated
def webbrowsing():
    while True:
        user = input("Type_Command: ")
        helplist = ["yt: Youtube", "fb:Facebook", "twi: Twitter", "gg: Google", "ig: Instagram"]
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


MainOfApp()
