def yaz(x):
    s= len(giris.get())
    giris.insert(s, str(x))
    print(x)

hesap = 5 
say1 = 0

def islemler(x):
    global hesap
    hesap=x
    global say1
    say1= float(giris.get())
    print(hesap)
    print(say1)
    giris.delete(0,"end")

say2=0
def hesapla():
    global say2
    say2=float(giris.get())
    global hesap
    sonuc=0
    if(hesap == 0): sonuc = say1 + say2
    elif(hesap == 1): sonuc = say1 - say2
    elif(hesap == 2): sonuc = say1 * say2
    elif(hesap == 3): sonuc = say1 / say2
    giris.delete(0,"end")
    giris.insert(0,str(sonuc))
    
def sil():
    giris.delete(0,"end")
    


from tkinter import *
pencere = Tk()
pencere.geometry("300x300")
giris = Entry(font="Verdana 14 bold", width=15, justify=RIGHT)
giris.place(x=20, y=20)

b=[]

for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",command=lambda x=i:yaz(x)))

sayac=0

for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50,y=50+i*50)
        sayac += 1


islem=[]

for i in range(0,4):
    islem.append(Button(font="Verdana 14 bold", width=2, command=lambda x=i:islemler(x)))
islem[0]["text"]="+"
islem[1]["text"]="-"
islem[2]["text"]="*"
islem[3]["text"]="/"


for i in range(0,4):
    islem[i].place(x=170, y=50+50*i)



sb= Button(text="0",font="Verdana 14 bold", width=2,command=lambda x=0:yaz(x))
sb.place(x=70,y=200)

no= Button(text=".",font="Verdana 14 bold", width=2,command=lambda x=".":yaz(x))
no.place(x=20,y=200)

es= Button(text="=",font="Verdana 14 bold", width=2, command=hesapla)
es.place(x=120,y=200)

sil= Button(text="sil",font="Verdana 14 bold", width=2, command=sil)
sil.place(x=20,y=250)

pencere.mainloop()