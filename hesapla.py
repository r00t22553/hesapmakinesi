#orta düzey hesap makinesi#

a = input("ilk Sayıyı Giriniz    : ")
a = float(a)
c = input("Yapılacak İşlem       : ")
b = input("İkinci Sayıyı Giriniz : ")
b = float(b)

if c=="+":
    print("Sonuç                 : ",a+b)
elif c=="-":
    print("Sonuç                 : ",a-b)
elif c=="/":
    print("Sonuç                 : ",a/b)
elif c=="*":
    print("Sonuç                 : ",a*b)
elif c=="**":
    print("Sonuç                 : ",a**b)
else:
    print("Hatalı İfade Kullandınız!")
