# http.server modülünü içe aktarıyoruz, bu sayede kendi ip adresinizi kod çalıştığı sürece web sunucusu olarak kullanabilirsiniz.
from http.server import BaseHTTPRequestHandler, HTTPServer
# Bir sınıf tanımlıyoruz, neden yaptığımızı bilmiyorsanız python rehberi izleyiniz.
class RequestHandler(BaseHTTPRequestHandler):
    
    # GET isteklerini işlemek için def ile metot tanımlıyoruz.
    def do_GET(self):
        # Bağlanan ip adresini aldık.
        ip = self.client_address[0]
        # Tarih ve saati aldık.
        from datetime import datetime
        now = datetime.now()
        # Tarih ve saati istenen formatta biçimlendirdik, burada gün/ay/yıl şeklinde.
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # Bağlanan ip adresini, tarih ve saati bir txt dosyasına kaydettik.
        with open("ipler.txt", "a") as f:
            f.write(f"{ip} - {dt_string}\n")
        # Website headerı
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Sitede göstermek isteyebileceğiniz bir mesajı buraya yazabilirsiniz.
        message = "Merhaba !"
        self.wfile.write(message.encode())

# Web sunucusu oluşturuyoruz.
server = HTTPServer(("0.0.0.0", 80), RequestHandler) # Kendi ip adresinizi ve istediğiniz portu girin.

server.serve_forever()