import sqlite3
from datetime import datetime
import time
import Burs



zaman = time.time()
tarih = str(datetime.fromtimestamp(zaman).strftime("%Y-%m-%d %H:%M:%S"))

saatim = datetime.now()
dakika = saatim.minute
saat = saatim.hour


while(True):

    time.sleep(10)

    def VeriEkle():
        con = sqlite3.connect("BURS.db")
        cursor = con.cursor()
        cursor.execute("insert into VeriCekme(Deger,Baslik,Tarih) values(?,?,?)", (len(Burs.dizi), Burs.dizi[0], tarih))
        print("Veri Kayıt İşlemi Başarı ile gerçekleştirildi.")
        con.commit()
        con.close()


    karsilastirma = []


    def VeriGetir():
        con = sqlite3.connect("BURS.db")
        cursor = con.cursor()
        cursor.execute("Select * From VeriCekme")
        veri = cursor.fetchall()
        for getir in veri:
            # print(getir)
            karsilastirma.append(getir)
        con.close()


    VeriEkle()
    VeriGetir()

    if karsilastirma[-1][2] == karsilastirma[-2][2]:
        Burs.MailGonder()

