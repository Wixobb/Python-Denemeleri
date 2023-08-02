while (True):
  def eratost(sinir): # bu arkadaş girdiğiniz sınıra kadar olan asal sayıları listeler, (fazla büyük girmeyiniz)
    is_asal = [True] * (sinir + 1)
    is_asal[0] = is_asal[1] = False
    for i in range(2, int(sinir**0.5) + 1):
      if is_asal[i]:
        for j in range(i * i, sinir + 1, i):
          is_asal[j] = False
    asallar = []
    for i in range(sinir + 1):
      if is_asal[i]:
        asallar.append(i)
    return asallar

  def asal_mi(sayi): # asal sayı tespiti yapar.
    if sayi < 2:
      return False, None
    for i in range(2, int(sayi**0.5) + 1):
      if sayi % i == 0:
        return False, i
    return True, None

  def asal_carpanlar(sayi): # girilen sayının asal çarpanlarınu bulur.
    carpanlar = []
    i = 2
    while i * i <= sayi:
      if sayi % i == 0:
        carpanlar.append(i)
        sayi //= i
      else:
        i += 1
    if sayi > 1:
      carpanlar.append(sayi)
    return carpanlar

  print("Hangisini kullanmak istiyorsunuz?\n1) Eratosthenes süzgeci\n2) Asal sayı tespiti\n3) Asal çarpanlar")
  secim = input("Lütfen 1, 2 veya 3 sayılarından birini girin: ")
  if secim == "1":
    sinir = int(input("Bir sinir girin: "))
    asallar = eratost(sinir)
    print(f"**{sinir} 'e kadar olan asal sayilar: {asallar}**")
  elif secim == "2":
    sayi = int(input("Bir sayı girin: "))
    durum, bolen = asal_mi(sayi)
    if durum:
      print(f"**{sayi} asal bir sayıdır.**")
    else:
      print(f"**{sayi} asal bir sayı değildir. Çünkü {bolen} sayısına tam bölünür.**")
  elif secim == "3":
    sayi = int(input("Bir sayı girin: "))
    carpanlar = asal_carpanlar(sayi)
    print(f"**{sayi} sayısının asal çarpanları: {carpanlar}**")
  else:
    print("Lütfen 1, 2 veya 3 sayılarından birini girin.")
  
  cikis = input("Çıkış yapmak istiyor musunuz? (E/H): ")
  if cikis == "E":
    break