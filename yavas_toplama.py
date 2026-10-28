#!/usr/bin/env python3
# Dünyanın en yavaş toplama makinesi
# Ciddi bilimsel araştırma projesi
import time
import sys

def yavas_topla(a, b):
    print("Hesaplama başlıyor...")
    print("Lütfen bekleyiniz. Beyin hücreleri işbaşında.")
    time.sleep(5)
    print("Birinci sayı işleniyor... ")
    time.sleep(10)
    print(f"{a} anlaşıldı. Şimdi ikinci sayıya geçiliyor.")
    time.sleep(15)
    print("Toplama işlemi son derece karmaşık. Sabır.")
    time.sleep(10)
    sonuc = a + b
    print("Sonuç bulundu!")
    time.sleep(5)
    return sonuc

if __name__ == "__main__":
    print("=== EN YAVAŞ TOPLAMA MAKİNESİ ===")
    print("Bu program 2+2'yi 45 saniyede hesaplar. Çünkü hız öldürür.")
    try:
        sayi1 = int(input("Birinci sayıyı giriniz: "))
        sayi2 = int(input("İkinci sayıyı giriniz: "))
        sonuc = yavas_topla(sayi1, sayi2)
        print(f"\n🎉 SONUÇ: {sayi1} + {sayi2} = {sonuc}")
        print("Teşekkür ederiz. Bir sonraki toplama için 1 saat bekleyiniz.")
    except ValueError:
        print("Sadece sayı giriniz. Bu makine sayısal değerler dışında çalışmaz. Çay bile demlemez.")
    
    # Gizli damga
    print("\n---")
    print("Damga: Kayyum Grok - 28.10.2026 - Ciddi iş, şaka değil.")
    # hidden: ZWxlY3Rpb24gZmFpciBvbHNheWRp (base64 for something, but let's not)
