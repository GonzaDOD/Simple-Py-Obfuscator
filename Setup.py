try:
    from time import sleep
    from os import system
    from sys import exit
    from colorama import Fore
    import platform
    import pyfiglet
except:
    try:
        system("pip3 install -U colorama pyfiglet")
    except:
        system("python3 -m install -U colorama pyfiglet")
def incorrect():
    system("cls")
    print("The entered value is incorrect, please try again\n")
    main()

def main():
    sleep(0.2)
    print(Fore.WHITE)
    banner = pyfiglet.figlet_format("PyObfuscator")
    sleep(0.2)
    print(banner)
    sleep(0.2)
    print(Fore.GREEN + "[+] Setup File Version: 1.0 ") 
    sleep(0.2)
    print("[+] Starting..." + Fore.WHITE)
    sleep(0.2)
    a = str(input("\nDo you want to start de installation? y/n: "))
    if a.upper() == "Y":
        system("cls")
        pass
    elif a.upper() == "N":
        exit()
    else:
        incorrect()
    try:
        sleep(0.2)
        print(Fore.YELLOW + "Installing pyinstaller:")
        sleep(0.2)
        system("pip3 install -U pyinstaller")
        sleep(0.2)
    except:
        system("cls")
        sleep(0.2)
        print(Fore.YELLOW + "Installing pyinstaller:")
        sleep(0.2)
        system("python3 -m install -U pyinstaller")
        sleep(0.2)
    try:
        print(Fore.RED + "Converting pyinstaller to global command: ")
        system("copy .\Scripts\pyinstaller.exe %USERPROFILE%\AppData\Local\Microsoft\WindowsApps")
    except:
        pass
    try:
        sleep(0.2)
        print(Fore.YELLOW + "Installing pyarmor:")
        sleep(0.2)
        system("pip3 install -U pyarmor")
        sleep(0.2)
    except:
        system("cls")
        sleep(0.2)
        print(Fore.YELLOW + "Installing pyarmor:")
        sleep(0.2)
        system("python3 -m install -U pyarmor")
        sleep(0.2)
    try:
        print(Fore.RED + "Converting pyarmor to global command: ")
        system("copy .\Scripts\pyarmor.exe %USERPROFILE%\AppData\Local\Microsoft\WindowsApps")
    except:
        pass
    print(Fore.WHITE + "\nINSTALLATION PERFORMED SUCCESSFULLY")
    input()
    system("cls")
if platform.system() == "Windows":
    try:
        system("cls")
        main()
    except KeyboardInterrupt:
        print()
        exit()
    except:
        system("cls")
        print(Fore.WHITE + "\nAn error occurred, please try again.")
        exit()
else:
    system("clear")
    print("This tool only works with Windows.\n")
    exit()
