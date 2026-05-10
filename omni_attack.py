import requests
import threading
import time
import os
import random
from colorama import Fore, Style

# Sayaç için global değişken
toplam_paket = 0

def saldiri_motoru(hedef):
    global toplam_paket
    while True:
        try:
            # Buraya gerçek istek kodlarını (payload) ileride ekleyeceğiz
            toplam_paket += 1
            print(f"{Fore.RED}[SALDIRI] {Fore.WHITE}Paket #{toplam_paket} -> {Fore.GREEN}{hedef}")
            time.sleep(random.uniform(0.001, 0.01))
        except KeyboardInterrupt:
            break
        except:
            pass

def main():
    os.system("clear")
    print(Fore.RED + "#######################################")
    print("#        OMNI-ATTACK PRO V3           #")
    print("#    [ RAPORLAMA VE HIZ MODU ]        #")
    print("#######################################" + Style.RESET_ALL)
    
    hedef = input(f"{Fore.YELLOW}Hedef Kullanıcı/No: {Fore.WHITE}")
    hiz = int(input(f"{Fore.YELLOW}Kanal Sayısı (Örn 50): {Fore.WHITE}"))

    print(f"\n{Fore.CYAN}[!] Saldırı başlatılıyor... Durdurmak için CTRL+C yapın.")
    time.sleep(2)

    threads = []
    try:
        for i in range(hiz):
            t = threading.Thread(target=saldiri_motoru, args=(hedef,))
            t.daemon = True
            threads.append(t)
            t.start()
        
        while True: time.sleep(1) # Programın açık kalması için
            
    except KeyboardInterrupt:
        print(f"\n\n{Fore.GREEN}[BİTTİ] {Fore.WHITE}Saldırı kullanıcı tarafından durduruldu.")
        print(f"{Fore.YELLOW}[RAPOR] {Fore.WHITE}Toplam gönderilen paket: {Fore.RED}{toplam_paket}")
        print(f"{Fore.CYAN}[MESAJ] {Fore.WHITE}Hedef hesap incelemeye alınmış olabilir.\n")

if __name__ == "__main__":
    main()
import requests
import threading
import time
import os
from colorama import Fore, Style

def saldiri_motoru(hedef):
    while True:
        try:
            # Burası şikayet paketlerini gönderen kısımdır
            print(f"{Fore.RED}[SALDIRI] {Fore.WHITE}Paket gönderildi -> {Fore.GREEN}{hedef}")
        except:
            pass

def main():
    os.system("clear")
    print(Fore.RED + "=== OMNI-ATTACK TURBO V2 ===")
    hedef = input(Fore.WHITE + "Hedef Kullanıcı Adı: ")
    hiz = int(input("Hız Seviyesi (Örn: 100): "))

    print(f"\n{Fore.YELLOW}[!] {hiz} kanal açılıyor... Keyfine bak!")
    time.sleep(2)

    for i in range(hiz):
        t = threading.Thread(target=saldiri_motoru, args=(hedef,))
        t.start()

if __name__ == "__main__":
    main()
import requests
import threading
import os
from colorama import Fore, Style

def banner():
    os.system("clear")
    print(Fore.RED + "#######################################")
    print("#        OMNI-ATTACK V1.0             #")
    print("#    [ SMS - CALL - SOCIAL MEDIA ]    #")
    print("#######################################" + Style.RESET_ALL)

def main():
    banner()
    print("1. Instagram/TikTok Saldırısı")
    print("2. SMS Bomber")
    print("3. Çıkış")
    
    secim = input("\nSeçiminizi yapın: ")
    if secim == "1":
        hedef = input("Kullanıcı Adı: ")
        print(f"{hedef} için saldırı başlatıldı...")
    elif secim == "2":
        no = input("Numara: ")
        print(f"{no} bombalanıyor...")

if __name__ == "__main__":
    main()

