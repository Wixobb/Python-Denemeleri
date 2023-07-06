while(True):
    b = (input("sayi gir:"))

    try:
        b = int(b)
        print("sayi girdin ha")
    except ValueError:
        try:
            b = float(b)
            print("noktali sayi girdin")
        except ValueError:
            print("sayi gir dedik")

#sayı girerken virgülü kullanamayacağınızı (5,6666 gibi) umarım biliyorsunuzdur :)



#bu da bi değişik versiyonu
while True:
    a = input("Sayi: ")

    try:
        a = float(a) or int(a)
        print("valla sayi girdin")
    except ValueError:
        print("Sayi girmedin")

