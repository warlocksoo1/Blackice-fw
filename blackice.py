import os

def main_menu():
    while True:
        os.system('clear')
        print("""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝ 
██╔═══╝ ██║     ██╔══██║██║     ██╔═██╗ 
██║     ███████╗██║  ██║╚██████╗██║  ██╗
╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
       🔥 BLACKICE TOOLKIT MENU 🔥

[1] 🛡️  Run Firewall Test
[2] 🔍 Run Port Scanner
[3] 📜 Show Firewall Log
[4] 🧼 Clear Firewall Log
[0] ❌ Exit
""")
        choice = input(">> Enter your choice: ")

        if choice == "1":
            os.system("firewall --test")
        elif choice == "2":
            ip = input("Enter target IP: ")
            start = input("Start port [default 20]: ") or "20"
            end = input("End port [default 100]: ") or "100"
            os.system(f"scanner {ip} --start {start} --end {end}")
        elif choice == "3":
            os.system("firewall --show-log")
        elif choice == "4":
            os.system("firewall --clear-log")
        elif choice == "0":
            print("Exiting Blackice... ❄️")
            break
        else:
            input("Invalid choice! Press Enter to try again...")

if __name__ == "__main__":
    main_menu()
