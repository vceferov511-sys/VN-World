def ana_sehife():
    print("\n" + "=" * 32)
    print("          V.N WORLD")
    print("=" * 32)
    print("1. V.N AI")
    print("2. Oyunlar")
    print("3. Mesajlaşma")
    print("4. Musiqi")
    print("5. Video və foto redaktə")
    print("6. Profil")
    print("7. Haqqımızda")
    print("0. Çıxış")

while True:
    ana_sehife()
    secim = input("\nSeçimini et: ")

    if secim == "1":
        print("V.N AI bölməsinə xoş gəlmisən!")
    elif secim == "2":
        print("Oyunlar bölməsi")
    elif secim == "3":
        print("Mesajlaşma bölməsi")
    elif secim == "4":
        print("Musiqi bölməsi")
    elif secim == "5":
        print("Video və foto redaktə bölməsi")
    elif secim == "6":
        print("Profil bölməsi")
    elif secim == "7":
        print("V.N World - Sənin dünyan!")
    elif secim == "0":
        print("Görüşənədək!")
        break
    else:
        print("Yanlış seçim!")

