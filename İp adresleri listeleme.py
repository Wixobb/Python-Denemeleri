import socket
import datetime

# Web sitenizin sunucusunun IP adresi ve portu
HOST1 = "192.168.56.1"
PORT = 80

# Dosya adı ve açma modu
FILE_NAME = "ip_log.txt"
FILE_MODE = "a"

# Bir soket oluşturun ve bağlantıları dinleyin
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST1, PORT))
s.listen()

# Bağlantıları kabul edin ve IP adreslerini dosyaya kaydedin
while True:
    conn, addr = s.accept()
    ip = addr[0]
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME, FILE_MODE) as f:
        f.write(f"{ip} {date}\n")
    conn.close()