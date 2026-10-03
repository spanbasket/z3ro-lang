# ==========================================
# z3r DİLİ MOTORU (v3.6 - Tam Kapsamlı Yardım Menüsü)
# ==========================================
import sys
import os
import subprocess

turkce_sozluk = {
    "değilse_eğer": "elif",
    "değilse": "else",
    "tekrarla": "for",
    "iken": "while",
    "tanımla": "def",
    "döndür": "return",
    "dahil_et": "import",
    "sınıf": "class",
    "yapı": "struct",
    "dene": "try",
    "hariç": "except",
    "nihayet": "finally",
    "yükselt": "raise",
    "aç": "open",
    "sil": "del",
    "küresel": "global",
    "ve": "and",
    "veya": "or",
    "değil": "not",
    "doğru": "True",
    "yanlış": "False",
    "boş": "None",
    "içinde": "in",
    "değildir": "is not",
    "dır": "is",
}

def yardim_menusu_goster():
    print("""
==================================================================
              z3r PROGRAMLAMA DİLİ - TAM YARDIM REHBERİ
==================================================================
Hoş geldin! z3r, Python gücünü kullanan yerli ve güçlü bir dildir.
İşte tüm komutlar ve Türkçe karşılıkları:

  [ Temel Komutlar ]
  • z3r yazdir "Metin"        -> Ekrana yazı yazdırır.
  • z3r al("Soru? ")          -> Kullanıcıdan girdi alır.
  • z3r x3 install paket.x3   -> x3 ile kütüphane indirir (Örn: discord.x3)
  • z3r komut [cmd]           -> Doğrudan CMD (Terminal) komutu çalıştırır.
  • z3r yardım                -> Bu yardım menüsünü açar.

  [ Türkçe Kod Sözlüğü (Python Eşdeğerleri) ]
  • eğer ... / değilse_eğer / değilse -> if / elif / else (Koşullar)
  • tekrarla                          -> for (Döngüler)
  • iken                              -> while (Döngüler)
  • tanımla                           -> def (Fonksiyon oluşturma)
  • döndür                            -> return (Fonksiyondan değer döndürme)
  • dahil_et                          -> import (Kütüphane ekleme)
  • sınıf                             -> class (Sınıf tanımlama)
  • dene / hariç                      -> try / except (Hata yakalama)
  • doğru / yanlış / boş              -> True / False / None
  • ve / veya / değil                 -> and / or / not (Mantıksal bağlaçlar)
==================================================================
""")

def komut_isleyici(komut_satiri):
    if komut_satiri in ["yardım", "z3ro yardım"]:
        yardim_menusu_goster()
        return

    if komut_satiri.startswith("x3 install "):
        paket = komut_satiri[len("x3 install "):].strip()
        if paket.endswith(".x3"):
            paket = paket[:-3]
        print(f"[x3 Paket Yöneticisi]: '{paket}' kütüphanesi indiriliyor...")
        subprocess.run(f"pip install {paket}", shell=True)
        return

    if komut_satiri.startswith("komut "):
        cmd_komutu = komut_satiri[len("komut "):]
        subprocess.run(cmd_komutu, shell=True)
        return

    temiz_satir = komut_satiri
    if temiz_satir.startswith("yazdır "):
        icerik = temiz_satir[len("yazdır "):]
        temiz_satir = f"print({icerik})"
    elif temiz_satir == "yazdır":
        temiz_satir = "print()"

    if temiz_satir.startswith("al "):
        icerik = temiz_satir[len("al "):]
        temiz_satir = f"input({icerik})"
    elif temiz_satir == "al":
        temiz_satir = "input()"

    for tr, py in turkce_sozluk.items():
        if temiz_satir.startswith(tr + " ") or temiz_satir == tr:
            temiz_satir = temiz_satir.replace(tr, py, 1)
            break

    try:
        exec(temiz_satir, globals(), {})
    except Exception as hata:
        print(f"[z3r Çalıştırma Hatası]: {hata}")

def interaktif_kabuk():
    print("==================================================")
    print("   z3r PROGRAMLAMA DİLİ - İNTERAKTİF KABUK (v3.6)")
    print("   Çıkmak için 'çıkış' yazabilirsin.")
    print("==================================================")
    while True:
        try:
            komut = input("z3r> ").strip()
            if komut == "çıkış":
                break
            if komut == "":
                continue
            komut_isleyici(komut)
        except Exception as hata:
            print(f"[Hata]: {hata}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        verilen_komut = " ".join(sys.argv[1:])
        komut_isleyici(verilen_komut)
    else:
        interaktif_kabuk()