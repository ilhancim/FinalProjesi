import pandas as pd
import Personel
import Doktor
import Hemsire
import Hasta

personel1 = Personel.Personel("1","Ilhan","Kilic","Personel",35000)
personel2 = Personel.Personel("2","Renas","Tas","Personel",20000)
personeller = [personel1,personel2]

doktor1 = Doktor.Doktor("3","Ahmet Mirza","Millet","Doktor",17000,"Goz",20,"Cigli Egitim ve Arastirma Hastanesi")
doktor2 = Doktor.Doktor("4","Muhammed Can","Arica","Doktor",14000,"Goz",15,"Cigli Egitim Hastanesi")
doktor3 = Doktor.Doktor("5","Eda","Karakoc", "Doktor",12000,"Fizyoterapist",12,"Cigli Egitim Hastanesi")
doktorlar = [doktor1,doktor2,doktor3]

hemsire1 = Hemsire.Hemsire("6","Mehmet Emirhan","Oguz","Hemsire",7000,"10","Yok","Cigli Egitim ve Arastirma Hastanesi")
hemsire2 = Hemsire.Hemsire("7","Secil","Tas","Hemsire",6500,"11","Yok","Cigli Egitim ve Arastirma Hastanesi")
hemsire3 = Hemsire.Hemsire("8","Muhammet Faik","Duman","Hemsire",5700,"12","Yok","Cigli Egitim ve Arastirma Hastanesi")
hemsireler = [hemsire1,hemsire2,hemsire3]

hasta1 = Hasta.Hasta("1","Semih","Ertan","06.02.2000","Kol kirik","Alci")
hasta2 = Hasta.Hasta("2","Mehmet Akif","Duman","26.09.1990","Miyopi","Gozluk")
hasta3 = Hasta.Hasta("3","Irem","Bagcivan","07.12.1980","Kizamik","Krem")
hastalar = [hasta1,hasta2,hasta3]

personelBilgi = []
for personel in personeller:
    personelBilgi.append([personel.personel_no, personel.ad, personel.soyad, personel.departman, personel.maas])

doktorBilgi = []
for doktor in doktorlar:
    doktorBilgi.append([doktor.personel_no, doktor.ad, doktor.soyad, doktor.departman, doktor.maas, doktor.uzmanlik, doktor.deneyim_yili, doktor.hastane])

hemsireBilgi = []
for hemsire in hemsireler:
    hemsireBilgi.append([hemsire.personel_no, hemsire.ad, hemsire.soyad, hemsire.departman, hemsire.maas, None, None, hemsire.calisma_saati, hemsire.sertifika, hemsire.hastane])

hastaBilgi = []
for hasta in hastalar:
    hastaBilgi.append([None, hasta.ad, hasta.soyad, None, None, None, None, None, None, None, hasta.hasta_no, hasta.dogum_tarihi, hasta.hastalik, hasta.tedavi])

bilgiler = personelBilgi + doktorBilgi + hemsireBilgi + hastaBilgi

columns = ["personel_no", "ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastane", "calisma_saati",
            "sertifika", "hasta_no", "dogum_tarihi", "hastalik", "tedavi"]

#dataFrame oluşturuldu
df = pd.DataFrame(bilgiler, columns=columns)

#Boş olan değişken değerleri 0 a atandı
df.fillna(0, inplace=True)

#Doktorlar uzmanlık alanlarına göre gruplandırılarak toplam sayısı hesaplandı ve yazdırıldı
doktorUzmanlik = df[df["uzmanlik"] != 0].groupby("uzmanlik").size()
print(f"Uzmanlik alanlarina gore doktor sayilari;\n{doktorUzmanlik}")

print("*******************************************************")

#5 yıldan fazla deneyime sahip doktorların toplam sayısı bulundu
doktorDeneyim =  df[(df["uzmanlik"] != 0) & (df["deneyim_yili"] > 5)]
print(f"5 yildan uzun deneyime sahip doktor sayisi: {len(doktorDeneyim)}")

print("*******************************************************")

#Hasta adına göre DataFrame alfabetik olarak sıralandı ve yazıldı
hastaAdi = df[df["hasta_no"] != 0].sort_values(by="ad")
print(f"Hasta adina göre alfabetik siralama;\n{hastaAdi}")

print("*******************************************************")

#Maaşı 7000 TL ve üzerinde olan personeller bulundu ve yazdırıldı
yuksekMaas = df[df["maas"] >= 7000]
print(f"Maasi 7000 TL ve uzerinde olan personeller;\n{yuksekMaas}")

print("*******************************************************")

#Dogum tarihi 1990 ve sonrası olan hastalar gösterildi ve yazdırıldı
df["dogum_tarihi"] = pd.to_datetime(df["dogum_tarihi"])
hasta1990Sonrasi = df[(df["hasta_no"] != 0) & (df["dogum_tarihi"] >= "1990-01-01")]
print(f"Dogum tarihi 1990 ve sonrası olan hastalar;\n{hasta1990Sonrasi}")

#Var olan DataFrame'den ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastalik, tedavi bilgilerini
#içeren yeni bir DataFrame elde edildi ve yazdırıldı
yeniDf = df[["ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastalik", "tedavi"]]
print(f"ad, soyad, departman, maas, uzmanlik, deneyim yili, hastalik ve tedavi bilgileri iceren yeni DataFrame;\n{yeniDf}")