import os
import time 


os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ROE BOT")

print("""
      
      LÜTFEN SEÇENEK SEÇİN

      1) TAKİPÇİ GÖNDER
      
      
      
      """)

secim = input("Lütfen İşlem Seçin : ")

if secim == "1":
    print("Tamamdır Teşekkürler....")
    os.system("bash bot.sh")

else :
    print("Geçersiz İşlem Lütfen İşlem Girin")

    

