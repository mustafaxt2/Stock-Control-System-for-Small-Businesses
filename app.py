import mysql.connector
from datetime import datetime

class Market:
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="05820753",
        database="vize"
    )
    cursor=connection.cursor()
    
    def __init__(self) -> None:
        self.urunler=[]
        self.sepetUrunleri=[]
        self.sepettekiUrunIsimleri=[]
        
    def kayitOl(self,ad,soyad,username,password,musteriOrSatici):
        sql=f"INSERT INTO {musteriOrSatici}s (firstname,lastname,username,password) VALUES(%s,%s,%s,%s)"
        values=(ad,soyad,username,password)
        Market.cursor.execute(sql,values)
        
        try:
            Market.connection.commit()
            print("A user has been added")
            print(f"Total users: {Market.cursor.rowcount}")
            return True
        except mysql.connector.Error as e:
            print(e)
            
    def girisYap(self,username,password,musteriOrSatici):
        Market.cursor.execute(f"SELECT username,password FROM {musteriOrSatici}s")
        result=Market.cursor.fetchall()
        try:
            for x in result:
                if username==x[0] and password==x[1]:
                    print("Hoşgeldiniz")
                    return True
                
        except mysql.connector.Error as e:
            print(e)
            
    def urunEkle(self,urunAdi,urunFiyati,urunAdedi):
        sql="INSERT INTO urunler (urun,fiyat,adet) VALUES(%s,%s,%s)"
        values=(urunAdi,urunFiyati,urunAdedi)
        Market.cursor.execute(sql,values)
        
        try:
            Market.connection.commit()
            print("A product has been added")
            return True
        except mysql.connector.Error as e:
            print(e)

    def fiyatGuncelle(self,urunAdi,yeniFiyat):
        sql="UPDATE urunler SET fiyat=%s WHERE urun=%s"
        values=(yeniFiyat,urunAdi)
        Market.cursor.execute(sql,values)
        try:
            Market.connection.commit()
            print(f"Urunler table has been updated")
        except mysql.connector.Error as e:
            print(e)
  
    def adetGuncelle(self,urunAdi,yeniAdet):
        sql="UPDATE urunler SET adet=%s WHERE urun=%s"
        values=(yeniAdet,urunAdi)
        Market.cursor.execute(sql,values)
        try:
            Market.connection.commit()
            print(f"Urunler table has been updated")
        except mysql.connector.Error as e:
            print(e)
     
    def sepeteEkle(self,urunAdi,urunFiyati,urunAdedi):
        sql="INSERT INTO sepet (urun,fiyat,adet) VALUES(%s,%s,%s)"
        values=(urunAdi,urunFiyati,urunAdedi)
        Market.cursor.execute(sql,values)
        
        try:
            Market.connection.commit()
            print("A product has been added")
            return True
        except mysql.connector.Error as e:
            print(e)

    def urunInfos(self):
        Market.cursor.execute("SELECT * FROM urunler")
        try:
            self.urunler= Market.cursor.fetchall()
        except mysql.connector.Error as e:
            print(e)

    def urunGuncelle(self,urunAdi):
        sql="UPDATE sepet SET adet=adet+1 WHERE urun=%s"
        values=(urunAdi,)
        Market.cursor.execute(sql,values)
        try:
            Market.connection.commit()
            print(f"Sepet table has been updated")
        except mysql.connector.Error as e:
            print(e)

    def sepetUrunleriniAl(self):
        Market.cursor.execute("SELECT urun,fiyat,adet FROM sepet")
        try:
            self.sepetUrunleri=Market.cursor.fetchall()
            for urun in self.sepetUrunleri:
                self.sepettekiUrunIsimleri.append(urun[0])
                
        except mysql.connector.Error as e:
            print(e)

    def sepettekiUrunuSil(self,urunAdi):
        sql="DELETE FROM sepet WHERE urun=%s"
        values=(urunAdi,)
        Market.cursor.execute(sql,values)
        try:
            Market.connection.commit()
            print(f"1 ürün sepetten çıkarıldı")
        except mysql.connector.Error as e:
            print(e)
    
    def urunSayisiniAzalt(self,urunAdi):
        sql="UPDATE urunler SET adet = adet-1 WHERE urun=%s"
        values=(urunAdi,)
        Market.cursor.execute(sql,values)
        try:
            Market.connection.commit()
            print(f"1 ürün databaseden eksildi")
        except mysql.connector.Error as e:
            print(e)
  
a=Market()