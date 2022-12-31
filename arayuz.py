from tkinter import *
from PIL import ImageTk,Image
from app import *
from tkinter.messagebox import showinfo

class AnaPencere(Tk):
    def __init__(self):
        super().__init__()
        Tk.resizable(self,width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("images\\market.jpg"))  # type: ignore
        self.width,self.height = self.img.width(),self.img.height()
        self.canvas=Canvas(width=self.width,height=self.height)
        self.canvas.pack()
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        self.title('Market')
        self.eval("tk::PlaceWindow . center'")
        self.canvas.create_text((self.width / 2, self.height/4), text='Hoşgeldiniz',font=("Helvetica 12 bold",50), anchor="center",fill="black")
        
        button2_img= (Image.open("images\\login.png"))  # type: ignore
        resized_button2_image= button2_img.resize((100,100), Image.Resampling.LANCZOS)  # type: ignore
        new_button2_image= ImageTk.PhotoImage(resized_button2_image)
        self.buton2=Button(command=GirisPenceresi,bg="white",padx=10,pady=10,cursor="hand2",image=new_button2_image)
        self.buton2.image=new_button2_image  # type: ignore
        self.canvas.create_window((self.width/2, self.height/2), window=self.buton2, anchor="center")
        self.canvas.create_text((self.width / 2, self.height/1.65), text='Giriş Yap',font=("Helvetica 12 bold",20), anchor="center",fill="black") 

class GirisPenceresi(AnaPencere):
    def __init__(self):
        self.girisPenceresi = Toplevel()
        self.girisPenceresi.resizable(width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("images\\girisyap.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.girisPenceresi.title("Giriş")
        self.canvas=Canvas(self.girisPenceresi,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        pencere.eval(f'tk::PlaceWindow {str(self.girisPenceresi)} center')
        def girisYap():
            username=ent3.get()
            password=ent4.get()
            musteriOrSatici=ent5.get()
            result=a.girisYap(username,password,musteriOrSatici)
            if result is True:
                showinfo(title="Giriş Islemi",message="Kullanıcı Basarıyla Giriş Yaptı")
                self.girisPenceresi.destroy()
                return Panel(musteriOrSatici)
            else:
                showinfo(title="Giriş Islemi",message="Bu Kullanıcı adına ait bir hesap yok")
                self.girisPenceresi.destroy()
        
        self.canvas.create_text((self._width/5 , self._height/3.15),text="Kullanıcı Adı",font=("Arial 12 bold",20), anchor="center")
        ent3=Entry(self.canvas,width=30)
        ent3.place(relx=0.1,rely=0.36)
        
        self.canvas.create_text((self._width/5 , self._height/2.35),text="Parola",font=("Arial 12 bold",20), anchor="center")
        ent4=Entry(self.canvas,width=30)
        ent4.config(show="*")
        ent4.place(relx=0.1,rely=0.45)
        
        def on_click(text):
            ent5.delete(0, END)
            ent5.insert(0,text)
            girisYap()
            
        b2=Button(self.canvas, text= "İş Veren", command=lambda: on_click("employer"),bg="blue",fg="white")
        b2.place(relx=0.123,rely=0.5)
        b3=Button(self.canvas, text= "Personel", command=lambda: on_click("employee"),bg="blue",fg="white")
        b3.place(relx=0.23,rely=0.5)
        
        ent5=Entry(self.canvas,width=30)
        ent5.place(relx=0.1,rely=0.56)
    
        b1=Button(self.canvas,text="Giriş",bg="black",fg="white",font="Arial 20 bold",command=girisYap)
        self.canvas.create_window((self._width/5 , self._height/1.5), window=b1, anchor="center")    
        
class Panel(AnaPencere):
    def __init__(self,saticiOrMusteri):
        self.saticiOrMusteri = saticiOrMusteri
        
        if self.saticiOrMusteri =="employer":
            self.panel = Toplevel()
            self.panel.resizable(width=False,height=False)
            self.img=ImageTk.PhotoImage(Image.open("images\\satıcımenu.jpg"))  # type: ignore
            self._width,self._height = self.img.width(),self.img.height()
            self.panel.title("Satıcı")
            self.canvas=Canvas(self.panel,width=self._width,height=self._height)
            self.canvas.pack()
            self.canvas.image=self.img  # type: ignore
            self.canvas.create_image((0,0),anchor=NW,image=self.img)
            pencere.eval(f'tk::PlaceWindow {str(self.panel)} center')
            
            def urunEkle():
                result=UrunEklemePenceresi()
                return result
            
            def fiyatGuncelle():
                result=FiyatGuncellemePenceresi()
                return result
            
            def adetGuncelle():
                result=AdetGuncellemePenceresi()
                return result
            
            def urunListesi():
                result=UrunPenceresi()
                return result
            
            def cariIslem():
                result=CariIslemPenceresi()
                return result
            
            
            self.canvas.create_text((self._width / 3, self._height/6), text='Hangi İşlemleri Yapmak İstersiniz?',font=("Helvetica 12 bold",31), anchor="center",fill="red")

            self.buton1=Button(self.canvas,text="Urun Ekle",command=urunEkle,bg="blue",font=("Helvetica 12 bold",20),cursor="hand2")
            self.canvas.create_window((self._width/3 , self._height/3), window=self.buton1, anchor="center")
            
            self.buton2=Button(self.canvas,text="Fiyat Guncelle",font=("Helvetica 12 bold",20),command=fiyatGuncelle,bg="blue",cursor="hand2")
            self.canvas.create_window((self._width/3 , self._height/2), window=self.buton2, anchor="center")
            
            self.buton3=Button(self.canvas,text="Adet Guncelle",font=("Helvetica 12 bold",20),command=adetGuncelle,bg="blue",cursor="hand2")
            self.canvas.create_window((self._width/3 , self._height/1.5), window=self.buton3, anchor="center")
            
            self.buton4=Button(self.canvas,text="Urun Listesi",font=("Helvetica 12 bold",20),command=urunListesi,bg="blue",cursor="hand2")
            self.canvas.create_window((self._width/3 , self._height/1.2), window=self.buton4, anchor="center")
            
            self.buton5=Button(self.canvas,text="Cari",font=("Helvetica 12 bold",20),command=cariIslem,bg="blue",cursor="hand2")
            self.canvas.create_window((self._width/3 , self._height/1.05), window=self.buton5, anchor="center")
 
        elif self.saticiOrMusteri =="employee":
            self.panel = Toplevel()
            self.panel.resizable(width=False,height=False)
            self.img=ImageTk.PhotoImage(Image.open("images\\musterimenu.jpg"))  # type: ignore
            self._width,self._height = self.img.width(),self.img.height()
            self.panel.title("Personel")
            self.canvas=Canvas(self.panel,width=self._width,height=self._height)
            self.canvas.pack()
            self.canvas.image=self.img  # type: ignore
            self.canvas.create_image((0,0),anchor=NW,image=self.img)
            pencere.eval(f'tk::PlaceWindow {str(self.panel)} center')
            
            def urunBak():
                result=MusteriUrunPenceresi()
                return result
            
            def sepetAc():
                result=Sepet()
                return result
            
            self.canvas.create_text((self._width / 3, self._height/6), text='Hangi İşlemleri Yapmak İstersiniz?',font=("Helvetica 12 bold",30), anchor="center",fill="red")

            self.buton1=Button(self.canvas,text="Satış Yap",command=urunBak,bg="white",font=("Helvetica 12 bold",20),cursor="hand2")
            self.canvas.create_window((self._width/3 , self._height/3), window=self.buton1, anchor="center")
                
            button2_img= (Image.open("images\\sepet.png"))  # type: ignore
            resized_button2_image= button2_img.resize((75,75), Image.Resampling.LANCZOS)  # type: ignore
            new_button2_image= ImageTk.PhotoImage(resized_button2_image)
            self.buton2=Button(self.canvas,command=sepetAc,bg='white',padx=20,pady=20,cursor="hand2",image=new_button2_image)
            self.buton2.image=new_button2_image  # type: ignore
            self.canvas.create_window((self._width/3, self._height/2), window=self.buton2, anchor="center")
            self.canvas.create_text((self._width / 3, self._height/1.65), text='Geçmiş',font=("Helvetica 12 bold",20), anchor="center",fill="black")
              
class Sepet:
    def __init__(self) -> None:
        self.sepetPenceresi=Toplevel()
        self.sepetPenceresi.geometry("500x250") 
        self.sepetPenceresi.title("Geçmiş")
        pencere.eval(f'tk::PlaceWindow {str(self.sepetPenceresi)} center')
        
        e=Label(self.sepetPenceresi,width=15,text='Urun',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=0)
        e=Label(self.sepetPenceresi,width=15,text='Fiyat',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=1)
        e=Label(self.sepetPenceresi,width=15,text='Adet',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=2)
        i=1
        k=0
        a.sepetUrunleriniAl()
        for urun in a.sepetUrunleri:
            for j in range(len(urun)):
                e = Label(self.sepetPenceresi,width=15, text=urun[j],borderwidth=2,relief='ridge', anchor="w") 
                e.grid(row=i, column=j)   
            i+=1
                      
class UrunEklemePenceresi:
    def __init__(self) -> None:
        self.urunEklemePenceresi = Toplevel()
        self.urunEklemePenceresi.resizable(width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("images\\stock.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.urunEklemePenceresi.title("Ürün Ekleme")
        self.canvas=Canvas(self.urunEklemePenceresi,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        self.urunEklemePenceresi.focus_set()   
        pencere.eval(f'tk::PlaceWindow {str(self.urunEklemePenceresi)} center')
         
        a.urunInfos()
        def on_click(text):
            u1.delete(0, END)
            u1.insert(0,text)
            
        def urunEkle():
            urunAdi=u1.get()
            urunFiyati=u2.get()
            urunAdedi=u3.get()
            
            try:
                a.urunEkle(urunAdi,urunFiyati,urunAdedi)
                showinfo(title="Basarılı",message="Ürün Veritabanına Kaydedildi")
                a.urunInfos()
                self.urunEklemePenceresi.destroy()
                return UrunEklemePenceresi()
            
            except mysql.connector.Error as e:
                showinfo(title="Hata",message=e)
                
        self.canvas.create_text((self._width/5 , self._height/10),text="Urun Adı",font=("Arial 12 bold",20), anchor="center",fill="white")
        u1=Entry(self.canvas,width=30)
        u1.place(relx=0.125,rely=0.135)
                
        self.canvas.create_text((self._width/4.8 , self._height/4.5),text="Urun Fiyatı",font=("Arial 12 bold",20), anchor="center",fill="white")
        u2=Entry(self.canvas,width=30)
        u2.place(relx=0.125,rely=0.25)

        self.canvas.create_text((self._width/4.8 , self._height/3.15),text="Urun Adedi",font=("Arial 12 bold",20), anchor="center",fill="white")
        u3=Entry(self.canvas,width=30)
        u3.place(relx=0.125,rely=0.36)

        ub=Button(self.canvas,text="Urunu Ekle",bg="black",fg="white",font="Arial 20 bold",command=urunEkle)
        self.canvas.create_window((self._width/4.8 , self._height/2), window=ub, anchor="center") 
        x=0.5
        y=0.135
        k=0
        self.button=[] 
        for urun in a.urunler:
            self.button.append(Button(self.canvas, text=f'{a.urunler[k][1]}->{a.urunler[k][2]}₺',padx=2,pady=2,bg="blue",fg="white",font=("Arial 12 bold",15),command=lambda k=k: on_click(a.urunler[k][1])))
            self.button[k].place(relx=x,rely=y)
            
            y+=0.1
            k+=1
            
class FiyatGuncellemePenceresi:
    def __init__(self) -> None:
        self.fiyatGuncellemePenceresi = Toplevel()
        self.fiyatGuncellemePenceresi.resizable(width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("images\\stock.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.fiyatGuncellemePenceresi.title("Fiyat Guncelleme")
        self.canvas=Canvas(self.fiyatGuncellemePenceresi,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        self.fiyatGuncellemePenceresi.focus_set()
        pencere.eval(f'tk::PlaceWindow {str(self.fiyatGuncellemePenceresi)} center')
        
        def on_click(text):
            u1.delete(0, END)
            u1.insert(0,text)
            
        def fiyatGuncelle():
            urunAdi=u1.get()
            yeniFiyat=u2.get()
            try:
                a.fiyatGuncelle(urunAdi,yeniFiyat)
                showinfo(title="Basarılı",message="Ürün Fiyatı Güncellendi")
                a.urunInfos()
                self.fiyatGuncellemePenceresi.destroy()
                return FiyatGuncellemePenceresi()
            
            except mysql.connector.Error as e:
                showinfo(title="Hata",message=e)
                
        self.canvas.create_text((self._width/5 , self._height/10),text="Urun Adı",font=("Arial 12 bold",20), anchor="center",fill="white")
        u1=Entry(self.canvas,width=30)
        u1.place(relx=0.125,rely=0.135)
                
        self.canvas.create_text((self._width/4.8 , self._height/4.5),text="Urun Fiyatı",font=("Arial 12 bold",20), anchor="center",fill="white")
        u2=Entry(self.canvas,width=30)
        u2.place(relx=0.125,rely=0.25)

        ub=Button(self.canvas,text="Fiyat Guncelle",bg="black",fg="white",font="Arial 20 bold",command=fiyatGuncelle)
        self.canvas.create_window((self._width/4.8 , self._height/2.5), window=ub, anchor="center")
        a.urunInfos()
        
        self.canvas.create_window((self._width/4.8 , self._height/2), window=ub, anchor="center") 
        x=0.5
        y=0.135
        k=0
        self.button=[] 
        for urun in a.urunler:
            self.button.append(Button(self.canvas, text=f'{a.urunler[k][1]}->{a.urunler[k][2]}₺',padx=2,pady=2,bg="blue",fg="white",font=("Arial 12 bold",15),command=lambda k=k: on_click(a.urunler[k][1])))
            self.button[k].place(relx=x,rely=y)
            
            y+=0.1
            k+=1

class AdetGuncellemePenceresi:
    def __init__(self) -> None:
        self.adetGuncellemePenceresi = Toplevel()
        self.adetGuncellemePenceresi.resizable(width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("images\\stock.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.adetGuncellemePenceresi.title("Adet Guncelleme")
        self.canvas=Canvas(self.adetGuncellemePenceresi,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        self.adetGuncellemePenceresi.focus_set()
        pencere.eval(f'tk::PlaceWindow {str(self.adetGuncellemePenceresi)} center')
        
        def on_click(text):
            u1.delete(0, END)
            u1.insert(0,text)
        
        def adetGuncelle():
            urunAdi=u1.get()
            yeniAdet=u2.get()
            try:
                a.adetGuncelle(urunAdi,yeniAdet)
                showinfo(title="Basarılı",message="Ürün Adeti Güncellendi\nDeğişiklikleri görmek için yeniden başlatınız")
                a.urunInfos()
                self.adetGuncellemePenceresi.destroy()
                return AdetGuncellemePenceresi()
            
            except mysql.connector.Error as e:
                self.adetGuncellemePenceresi.focus_set()
                showinfo(title="Hata",message=e)
                
        self.canvas.create_text((self._width/5 , self._height/10),text="Urun Adı",font=("Arial 12 bold",20), anchor="center",fill="white")
        u1=Entry(self.canvas,width=30)
        u1.place(relx=0.125,rely=0.135)
                
        self.canvas.create_text((self._width/4.8 , self._height/4.5),text="Urun Adedi",font=("Arial 12 bold",20), anchor="center",fill="white")
        u2=Entry(self.canvas,width=30)
        u2.place(relx=0.125,rely=0.25)

        ub=Button(self.canvas,text="Adet Güncelle",bg="black",fg="white",font="Arial 20 bold",command=adetGuncelle)
        self.canvas.create_window((self._width/4.8 , self._height/2.5), window=ub, anchor="center")
        a.urunInfos()
        x=0.5
        y=0.135
        k=0
        self.button=[] 
        for urun in a.urunler:
            self.button.append(Button(self.canvas, text=f'{a.urunler[k][1]}->{a.urunler[k][3]} Adet',padx=2,pady=2,bg="blue",fg="white",font=("Arial 12 bold",15),command=lambda k=k: on_click(a.urunler[k][1])))
            self.button[k].place(relx=x,rely=y)
            
            y+=0.1
            k+=1

class UrunPenceresi:
    def __init__(self) -> None:
        self.urunPenceresi=Toplevel()
        self.urunPenceresi.geometry("400x250") 
        self.urunPenceresi.title("Ürün Listesi")
        pencere.eval(f'tk::PlaceWindow {str(self.urunPenceresi)} center')
        
        a.urunInfos()
        e=Label(self.urunPenceresi,width=15,text='id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=0)
        e=Label(self.urunPenceresi,width=15,text='Urun',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=1)
        e=Label(self.urunPenceresi,width=15,text='Fiyat',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=2)
        e=Label(self.urunPenceresi,width=15,text='Adet',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=3)
        i=1
        for urun in a.urunler: 
            for j in range(len(urun)):
                e = Label(self.urunPenceresi,width=15, text=urun[j],borderwidth=2,relief='ridge', anchor="w") 
                e.grid(row=i, column=j)                           
            i+=1
            
class CariIslemPenceresi:
    def __init__(self):
        self.cariIslemPenceresi = Toplevel()
        self.cariIslemPenceresi.resizable(width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("images\\cari.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.cariIslemPenceresi.title("Cari İşlemler")
        self.canvas=Canvas(self.cariIslemPenceresi,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)     
        pencere.eval(f'tk::PlaceWindow {str(self.cariIslemPenceresi)} center')
               
        a.sepetUrunleriniAl()
        x=0.075
        y=0.15
        toplamGelir=0
        for urun in a.sepetUrunleri: 
            for j in range(len(urun)):
                e = Label(self.canvas,width=35, text=f"Satılan {urun[0]} sayısı:{urun[2]} Adet",borderwidth=2,relief='ridge', anchor="w",fg="red",font=("Helvetica 12 bold",15)) 
                e.place(relx=x,rely=y)
                r = Label(self.canvas,width=25, text=f"Elde edilen gelir:{urun[1]*urun[2]}₺",borderwidth=2,relief='ridge', anchor="w",fg="red",font=("Helvetica 12 bold",15)) 
                r.place(relx=0.5,rely=y)
            toplamGelir+=(urun[1]*urun[2])     
            y+=0.075
        t=Label(self.canvas,width=25, text=f"Elde edilen toplam gelir:{toplamGelir}₺",borderwidth=2,relief='ridge', anchor="w",fg="green",font=("Helvetica 12 bold",20)) 
        t.place(relx=0.075,rely=0.8)
        
class MusteriUrunPenceresi:
    def __init__(self) -> None:
        self.musteriUrunPenceresi = Toplevel()
        self.musteriUrunPenceresi.resizable(width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("images\\stock.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.musteriUrunPenceresi.title("Ürün Satış")
        self.canvas=Canvas(self.musteriUrunPenceresi,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        self.musteriUrunPenceresi.focus_set()   
        pencere.eval(f'tk::PlaceWindow {str(self.musteriUrunPenceresi)} center')
         
        a.urunInfos()
        e=Label(self.canvas,width=15,text='id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=0)
        e=Label(self.canvas,width=15,text='Urun',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=1)
        e=Label(self.canvas,width=15,text='Fiyat',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=2)
        e=Label(self.canvas,width=15,text='Adet',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=3)
        i=1
        k=0
        self.button = []
        def open_this(urunAdi,urunFiyati):
            a.sepetUrunleriniAl()
            if urunAdi not in a.sepettekiUrunIsimleri:
                a.sepeteEkle(urunAdi,urunFiyati,1)
                showinfo(title="Satıldı!",message=f"{urunAdi} satıldı")
                a.urunSayisiniAzalt(urunAdi)
                a.sepetUrunleriniAl()
                self.musteriUrunPenceresi.focus_set()
                self.musteriUrunPenceresi.destroy()
                return MusteriUrunPenceresi()
                
            else:
                a.urunGuncelle(urunAdi)
                showinfo(title="Satıldı!",message=f"{urunAdi} satıldı")
                a.urunSayisiniAzalt(urunAdi)
                a.sepetUrunleriniAl()
                self.musteriUrunPenceresi.focus_set()
                self.musteriUrunPenceresi.destroy()
                return MusteriUrunPenceresi()
                
        for urun in a.urunler:
            self.button.append(Button(self.canvas, text='Sat',padx=2,pady=2,command=lambda k=k: open_this(a.urunler[k][1],a.urunler[k][2])))
            self.button[k].grid(column=4, row=i, sticky=W)
            
            for j in range(len(urun)):
                e = Label(self.canvas,width=15, text=urun[j],borderwidth=2,relief='ridge', anchor="w") 
                e.grid(row=i, column=j)   
            i+=1
            k+=1
            
pencere=AnaPencere()

pencere.mainloop()