import time

starttime=time.time()
lasttime=starttime
lapnum=1
 
print("Her ENTER = 1 Tur \nCTRL+C ile program kapanir.")
 
try:
     while True:
             
          input()
 
          laptime=round((time.time() - lasttime), 2)
 
          # Başlangıçtan beri geçen toplam süre.
          totaltime=round((time.time() - starttime), 2)
 
          # Tur sayısını printler,
          # Tur süresi ve toplam süre.
          print("Tur Sayısı "+str(lapnum))
          print("Toplam Süre: "+str(totaltime))
          print("Tur Süresi: "+str(laptime))
           
          print("*"*20)
 
          # Toplam süre ve tur sayısını günceller.
          lasttime=time.time()
          lapnum+=1
 
# CTRL+C basarsanız:
except KeyboardInterrupt:
     print("Tur Sayaci kapatildi.")