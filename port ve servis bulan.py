import socket
ip = input("Lütfen bir IP adresi girin: ")

# Açık portlar için liste
open_ports = []

# Her bir port için socket oluşturup ve bağlanmaya çalışıyoruz.
for port in range(1, 101): #buradaki aralık ilk 100 portu tarar, aralığı istediğiniz gibi değiştirebilirsiniz.
    s = socket.socket()
    s.settimeout(0.2) # Zaman aşımı
    try:
        s.connect((ip, port)) # Bağlanmayı dene
        open_ports.append(port) # Bağlantı başarılıysa, portu listeye ekle
        s.close() # Socketi kapat
    except:
        pass # Bağlantı başarısızsa veya zaman aşımına uğrarsa, bir şey yapma

# Açık portları ekrana yazdır.
print(f"IP adresinin ilk 100 portundan açık olanlar: {open_ports}")

# Açık portlarda çalışan servisleri bulmak için socket.getservbyport() fonksiyonunu kullanıyoruz.
for port in open_ports:
    service = socket.getservbyport(port)
    print(f"Port {port} üzerinde çalışan servis: {service}")

# Tüm bilgileri bir TXT dosyasına kaydediyoruz.
with open("bilgiler.txt", "w") as f:
    f.write(f"IP adresi: {ip}\n")
    f.write(f"İlk 100 portundan açık olanlar: {open_ports}\n")
    for port in open_ports:
        service = socket.getservbyport(port)
        f.write(f"Port {port} üzerinde çalışan servis: {service}\n")

print("Tüm bilgiler bilgiler.txt dosyasına kaydedildi.")
