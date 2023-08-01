import math

def faktoriyel(n):
    if n < 0:
        return "Geçersiz girdi"
    else:
        return math.factorial(n) #math modülünde faktöriyal fonksiyonu buldum, onu ekledim.

def sekil_alan(adi, *kenarlar): #hepsi için tek tek def yazmak yerine hepsini tek def altına topladım.
    if adi == "kare":
        k = kenarlar[0]
        return k * k
    elif adi == "dikdortgen":
        k, u = kenarlar
        return k * u
    elif adi == "yamuk":
        a_t, u_t, y = kenarlar
        return ((a_t + u_t) * y) / 2
    elif adi == "paralelkenar":
        k, y = kenarlar
        return k * y
    elif adi == "eskenardortgen":
        a_k, y_k = kenarlar
        return (a_k * y_k) / 2
    else:
        return "Geçersiz şekil"

def metrik_donustur(x, birim):
    birimler = {"cm": 0.01, "mm": 0.001, "km": 1000, "inc": 0.0254}
    if birim in birimler:
        return x * birimler[birim]
    else:
        return "Geçersiz birim"

def karekok(x):
    if x < 0:
        return "Geçersiz girdi"
    else:
        return math.sqrt(x)

def daire(r):
    pi = math.pi
    alan = pi * r ** 2
    cevre = 2 * pi * r
    return (alan, cevre)

def sin_cos(x): #sin ve cos değerlerini tek def altına topladım.
    x = x * math.pi / 180 #dereceyi radyan yapıyoruz.
    sin = math.sin(x)
    cos = math.cos(x)
    return (sin, cos)

# Kullanıcı Menüsü

while True: #Döngü ekledim ki program her işlemden sonra sonlanmasın.
    print("Merhabalar, ne yapmak istersiniz?:")
    print("1. Faktöriyel Bulma")
    print("2. Geometrik Şekillerin Alanını Hesaplayın")
    print("3. Metrik Dönüşüm")
    print("4. Karekök Değeri Bulma")
    print("5. Yarıçapı Girilen Dairenin Alanı ve Çevresini Bulma")
    print("6. Sin Cos Dönüştürme ve Değer Bulma")
    print("7. Asal Sayı Tespiti")
    print("Yapmak istediğiniz işlemin numarasını girin:")
    secim = int(input())

    if secim == 1: 
        print("Faktöriyelini bulmak istediğiniz sayıyı girin:")
        n = int(input())
        sonuc = faktoriyel(n)
        print(f"{n}! = {sonuc}")
    
    elif secim == 2:
        print("""
       1 - Kare
       2 - Dikdörtgen
       3 - Yamuk
       4 - Paralelkenar
       5 - Eşkenar Dörtgen
       6 - Üçgen
        """)
        
        secimx = int(input("Alanını hesaplamak istediğiniz şekil: "))
        
        if secimx == 1:
            k = int(input("Karenin bir kenarı: "))
            sonuc = sekil_alan("kare", k) 
            print(f"Karenin alanı = {sonuc}")
        
        elif secimx == 2:
            k = int(input("Dikdörtgenin kısa kenarı: "))
            u = int(input("Dikdörtgenin uzun kenarı: "))
            sonuc = sekil_alan("dikdortgen", k, u)
            print(f"Dikdörtgenin alanı = {sonuc}")
        
        elif secimx == 3:
            a = int(input("Yamuğun alt taban uzunuğu: "))
            u = int(input("Yamuğun üst taban uzunuğu: "))
            y = int(input("Yamuğun yüksekliği: "))
            sonuc = sekil_alan("yamuk", a, u, y)
            print(f"Yamuğun alanı = {sonuc}")
        
        elif secimx == 4:
            k = int(input("Paralel kenarın alt taban uzunluğu: "))
            y = int(input("Paralel kenarın yüksekliği: "))
            sonuc = sekil_alan("paralelkenar", k, y)
            print(f"Paralel kenarın alanı = {sonuc}")
        
        elif secimx == 5:
            a = int(input("Eşkenar dörtgenin alt kenar uzunluğu: "))
            y = int(input("Eşkenar dörtgenin yan kenar uzunluğu: "))
            sonuc = sekil_alan("eskenardortgen", a, y)
            print(f"Eşkenar dörtgenin alanı = {sonuc}")
            
        elif secimx == 6:
            print("1. Taban x Yükseklik ile Alan Hesaplama ")
            print("2. Kenar uzunlukları ile Alan Hesaplama ")
            secimy = int(input())
            
            if secimy == 1:
                taban = float(input("Taban uzunluğunu girin: "))
                yükseklik = float(input("Yüksekliği girin: "))
                alan1 = (taban * yükseklik) / 2
                print("Üçgenin Alanı:", alan1)

            if secimy == 2:
                a = float(input("Kenar giriniz: "))
                b = float(input("Kenar giriniz: "))
                c = float(input("Kenar giriniz: "))
                s = (a + b + c) / 2
                alan2 = (s * (s - a) * (s - b) * (s - c)) ** 0.5
                print("Üçgenin Alanı: ", alan2)
        
        else:
            print("Geçersiz seçim")
    
    elif secim == 3:
        print("Metrik dönüşüm yapmak istediğiniz değeri girin:")
        x = float(input())
        print("Değerin birimini girin (cm, mm, km veya in):")
        birim = input()
        sonuc = metrik_donustur(x, birim)
        print(f"{x} {birim} = {sonuc} m")
    
    elif secim == 4:
        print("Karekökünü bulmak istediğiniz sayıyı girin:")
        x = float(input())
        sonuc = karekok(x)
        print(f"√{x} = {sonuc}")
    
    elif secim == 5:
        print("Yarıçapı girin:")
        r = float(input())
        alan, cevre = daire(r)
        print(f"Yarıçapı {r} olan dairenin alanı = {alan}, çevresi = {cevre}")
    
    elif secim == 6:
        print("Sin ve Cos açılarını birbirine çevirip değer bulmak için hangisini gireceksiniz?")
        print("1. Sin")
        print("2. Cos")
        alt_secim = int(input())
        
        if alt_secim == 1:
            print("Sin değerini hesaplamak istediğiniz açıyı girin (derece cinsinden):")
            x = float(input())
            sin, cos = sin_cos(x) #sin_cos fonksiyonu buldum onu ekledim burada.
            print(f"Sin({x})° = {sin}, Cos({x})° = {cos}")
        
        elif alt_secim == 2:
            print("Cos değerini hesaplamak istediğiniz açıyı girin (derece cinsinden):")
            x = float(input())
            cos, sin = sin_cos(x)
            print(f"Cos({x})° = {cos}, Sin({x})° = {sin}")

    elif secim == 7:
        sayi = int(input("Sayı giriniz: "))
        asal = True #aşağıda if asal yazabilmek için bayrak değişkeni tanımladım.
        if sayi > 1:
            for i in range(2, (sayi // 2) + 1): #2'den sayının yarısına kadar olan tüm sayılara bölüyoruz.
                if sayi % i == 0:
                    asal = False
                    print(sayi, "\033[1masal sayı değildir, çünkü", i, "sayısına tam bölünür\033[0m!")
                    break
            if asal:
                print(sayi, "asal sayıdır.")
        
        else:
            print("Geçersiz seçim")
    
    else:
        print("Geçersiz seçim")