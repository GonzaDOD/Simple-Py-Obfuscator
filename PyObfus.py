try:
    import platform
    from time import sleep
    import pyfiglet
    from os import system
    from sys import exit
    from colorama import Fore
except ImportError:
	print("\n[+] Import Error!")
	print("\n[+] Pre Requistes were not found! Running Setup.py...")
	system("python3 Setup.py")

def incorrect():
    system("cls")
    print("The entered value is incorrect, please try again\n")
    main()
def start():
    banner = pyfiglet.figlet_format("PyObfuscator")
    print(banner)
    sleep(0.2)
    print(Fore.GREEN + "[+] Setup File Version: 1.0 ") 
    sleep(0.2)
    print("[+] Supported OS : Windows")
    sleep(0.2)
    print("[+] GitHub Profile : https://github.com/GonzaDOD")
    sleep(0.2)
    print("[+] Starting..." + Fore.WHITE)
    sleep(0.2)
    input(Fore.WHITE + "\nPyObfus>: Press enter to continue ")
    system("cls")
    main()

def main():
    print(Fore.WHITE)
    banner = pyfiglet.figlet_format("PyObfuscator")
    sleep(0.2)
    print(banner)
    sleep(0.2)
    print(Fore.RED + "\t1) Obfuscate Python Script ")
    sleep(0.2)
    print("\t2) Compile .py to .exe")
    sleep(0.2)
    print("\t3) Obfuscate and Compile .py to .exe")
    sleep(0.2)
    print("\t4) Exit Program")
    sleep(0.2)
    print("\nFor EX. >> 3")
    sleep(0.2)
    user_input = input(Fore.WHITE + "\nPyObfus>: ")
    if "1" == user_input:
        path = input("\nPyObfus>: Please enter script path --> ")
        system(f'pyarmor obfuscate {path} --exact')

    elif "2" == user_input:
        icon = input("\nPyObfus>: Do you want to add icon to EXE? y/n >> ")
        if "Y" == icon.upper():
            path = input("\nPyObfus>: Please enter script path --> ")
            icon_path = input("\nPyObfus>: Please enter icon path (Only .ico files are supported) --> ")
            console = input("Do you want to hide the console? y/n")
            if "Y" == console.upper():
                system(f"pyinstaller --noconfirm --onefile --windowed --icon \"{icon_path}\" \"{path}\"")
            elif "N" == console.upper():
                system(f"pyinstaller --noconfirm --onefile --console --icon \"{icon_path}\" \"{path}\"")
            else:
                incorrect()

        elif "N" == icon.upper():
            path = input("\nPyObfus>: Please enter script path --> ")
            console = input("Do you want to hide the console? y/n")
            if "Y" == console.upper():
                system(f"pyinstaller --noconfirm --onefile --windowed \"{path}\"")
            elif "N" == console.upper():
                system(f"pyinstaller --noconfirm --onefile --console \"{path}\"")
            else:
                incorrect()
        else:
            incorrect()
    elif "3" == user_input:
        icon = input("\nPyObfus>: Do you want to add icon to EXE? y/n >> ")
        if "Y" == icon.upper():
            path = input("\nPyObfus>: Please enter script path --> ")
            icon_path = input("\nPyObfus>: Please enter icon path (Only .ico files are supported) --> ")
            console = input("Do you want to hide the console? y/n")
            if "Y" == console.upper():
                system(f'pyarmor obfuscate {path} --exact')
                system(f"pyinstaller --noconfirm --onefile --windowed --icon \"{icon_path}\" --add-data \"./dist/pytransform\" \"{path}\"")
            elif "N" == console.upper():
                system(f'pyarmor obfuscate {path} --exact')
                system(f"pyinstaller --noconfirm --onefile --console --add-data ./dist/pytransform {path}")
            else:
                incorrect()

        elif "N" == icon.upper():
            path = input("\nPyObfus>: Please enter script path --> ")
            console = input("Do you want to hide the console? y/n")
            if "Y" == console.upper():
                system(f'pyarmor obfuscate {path} --exact')
                system(f"pyinstaller --noconfirm --onefile --windowed --add-data ./dist/pytransform {path}")
            elif "N" == console.upper():
                system(f'pyarmor obfuscate {path} --exact')
                system(f"pyinstaller --noconfirm --onefile --console --add-data ./dist/pytransform {path}")
            else:
                incorrect()

        else:
            incorrect()
    elif "4" == user_input:
        print("\nPyObfus>: Shutting Down Program")
        exit()
    else:
        incorrect()

if platform.system() == "Windows":
    try:
        system("cls")
        start()
    except KeyboardInterrupt:
        system("cls")
        exit()
    except:
        system("cls")
        print(Fore.WHITE + "\nAn error occurred, please try again.")
        exit()
else:
    system("clear")
    print("This tool only works with Windows")
    print("Try with https://github.com/Vedant-Bhalgama/VySecator")
    exit()