print("Hazine Adasına Hoşgeldiniz.")
print("Sizin Amacınız Adada Hayatta Kalmak Ve Hazineyi Bulmak.\n" "Hazırsanız Başlayalım.")

secim1 = input('Bir\'Yol Ayrımına Ulaştınız. Ne tarafa gitmek istersiniz? "sağ" yada "sol"').lower()
if secim1 == "sol":
    secim2 = input('Bir\'Göle ulaştınız Ne yapmak istersiniz? "bekle" Yada "yüz"').lower()
    if secim2 == "bekle":
        print("Gölde biraz beklediniz ve biraz yorgunluk hissettiniz. Ama bir şey olmadı. Sıkıldınız ve yola devam ettiniz.")
        secim3 = input('Yeniden Bir\'Yol Ayrımına Ulaştınız. Ne tarafa gitmek istersiniz? "sağ" yada "sol"').lower()
        if secim3 == "sağ":
            print("Çıkmaz Yoldasınız. Oyunu Kaybettiniz.")
            if secim3 == "sol":
                print('Bir\'Süre Gittiniz Garip Bir Şekli Olan Bir Ağaç Gördünüz. Ne Yapmak İstersiniz? "incele" Yada "geç"').lower()
            if secim3 == "incele":
                print("Bu işte bir gariplik var! Cebinizdeki Kazma Ve Küreği çıkarttınız ve ağacın dibine kazmaya başladınız! Tebrikler hazineyi buldunuz :)")


    else:
        print("Korkunç Bir Yılan Sizi Yedi. Oyun Bitti.")
      












