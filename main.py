import pandas as pd
import Personel
import Doktor
import Hemsire
import Hasta

def main():
    try:
        #Personel nesneleri tanımlandı ve personeller listesine eklendi
        personel1 = Personel.Personel("1001","Ilhan","Kilic","Personel",35000)
        personel2 = Personel.Personel("1002","Renas","Tas","Personel",20000)
        personeller = [personel1,personel2]

        #Doktor nesneleri tanımlandı ve doktorlar listesine eklendi
        doktor1 = Doktor.Doktor("2103","Ahmet Mirza","Millet","Doktor",17000,"Goz",20,"Cigli Egitim ve Arastirma Hastanesi")
        doktor2 = Doktor.Doktor("2104","Muhammed Can","Arica","Doktor",14000,"Goz",15,"Cigli Egitim Hastanesi")
        doktor3 = Doktor.Doktor("2205","Eda","Karakoc", "Doktor",12000,"Fizyoterapist",12,"Cigli Egitim Hastanesi")
        doktorlar = [doktor1,doktor2,doktor3]

        #Hemsire nesneleri tanımlandı ve hemsireler listesine eklendi
        hemsire1 = Hemsire.Hemsire("3006","Mehmet Emirhan","Oguz","Hemsire",7000,"10","Yok","Cigli Egitim ve Arastirma Hastanesi")
        hemsire2 = Hemsire.Hemsire("3007","Secil","Tas","Hemsire",6500,"11","Yok","Cigli Egitim ve Arastirma Hastanesi")
        hemsire3 = Hemsire.Hemsire("3008","Muhammet Faik","Duman","Hemsire",5700,"12","Yok","Cigli Egitim ve Arastirma Hastanesi")
        hemsireler = [hemsire1,hemsire2,hemsire3]

        #Hasta nesneleri tanımlandı ve hastalar listesine eklendi
        hasta1 = Hasta.Hasta("4101","Semih","Ertan","06.02.2000","Kol kirik","C_Alci")
        hasta2 = Hasta.Hasta("4202","Mehmet Akif","Duman","26.09.1990","Miyopi","A_Gozluk")
        hasta3 = Hasta.Hasta("4303","Irem","Bagcivan","07.12.1980","Kizamik","E_Krem")
        hastalar = [hasta1,hasta2,hasta3]

        #Personellerin bilgileri personelBilgi listesine eklendi
        personelBilgi = []
        for personel in personeller:
            personelBilgi.append([personel.personel_no, personel.ad, personel.soyad, personel.departman, personel.maas])

        #Doktorların bilgileri doktorBilgi listesine eklendi
        doktorBilgi = []
        for doktor in doktorlar:
            doktorBilgi.append([doktor.personel_no, doktor.ad, doktor.soyad, doktor.departman, doktor.maas, doktor.uzmanlik, doktor.deneyim_yili, doktor.hastane])

        #Hemsirelerin bilgileri hemsireBilgi listesine eklendi
        hemsireBilgi = []
        for hemsire in hemsireler:
            hemsireBilgi.append([hemsire.personel_no, hemsire.ad, hemsire.soyad, hemsire.departman, hemsire.maas, None, None, hemsire.hastane, hemsire.calisma_saati, hemsire.sertifika])

        #Hastaların bilgileri hastaBilgi listesine eklendi
        hastaBilgi = []
        for hasta in hastalar:
            hastaBilgi.append([None, hasta.ad, hasta.soyad, None, None, None, None, None, None, None, hasta.hasta_no, hasta.dogum_tarihi, hasta.hastalik, hasta.tedavi])

        #Tüm bilgiler bilgiler listesine eklendi
        bilgiler = personelBilgi + doktorBilgi + hemsireBilgi + hastaBilgi

        #DataFrame'in sutünları belirlendi
        columns = ["personel_no", "ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastane", "calisma_saati",
                    "sertifika", "hasta_no", "dogum_tarihi", "hastalik", "tedavi"]

        #dataFrame oluşturuldu
        df = pd.DataFrame(bilgiler, columns=columns)

        #Boş olan değişken değerleri 0 a atandı
        df.fillna(0, inplace=True)

        #Doktorlar uzmanlık alanlarına göre gruplandırılarak toplam sayısı hesaplandı ve yazdırıldı
        doktorUzmanlik = df[df["uzmanlik"] != 0].groupby("uzmanlik").size()
        print(f"\nUzmanlik alanlarina gore doktor sayilari;\n{doktorUzmanlik}")

        print("\n*******************************************************\n")

        #5 yıldan fazla deneyime sahip doktorların toplam sayısı bulundu
        doktorDeneyim =  df[(df["uzmanlik"] != 0) & (df["deneyim_yili"] > 5)]
        print(f"5 yildan uzun deneyime sahip doktor sayisi: {len(doktorDeneyim)}")

        print("\n*******************************************************\n")

        #Hasta adına göre DataFrame alfabetik olarak sıralandı ve yazıldı
        #.drop komuduyla hasta bilgileri olmayan kısımların gösterilmemesi sağlandı
        hastaAdi = (df[df["hasta_no"] != 0].sort_values(by="ad")
                    .drop(columns=["personel_no","departman","maas","uzmanlik","deneyim_yili","hastane","calisma_saati","sertifika"]))
        print(f"Hasta adina göre alfabetik siralama;\n{hastaAdi}")

        print("\n*******************************************************\n")

        #Maaşı 7000 TL ve üzerinde olan personeller bulundu ve yazdırıldı
        #.drop komuduyla personel bilgileri olmayan kısımların gösterilmemesi sağlandı
        maas7000Ust = (df[df["maas"] >= 7000]
                      .drop(columns=["uzmanlik","deneyim_yili","hastane","calisma_saati","sertifika","hasta_no","dogum_tarihi","hastalik","tedavi"]))
        print(f"Maasi 7000 TL ve uzerinde olan personeller;\n{maas7000Ust}")

        print("\n*******************************************************\n")

        #Dogum tarihi 1990 ve sonrası olan hastalar gösterildi ve yazdırıldı
        #.drop komuduyla hasta bilgileri olmayan kısımların gösterilmemesi sağlandı
        df["dogum_tarihi"] = pd.to_datetime(df["dogum_tarihi"])
        hasta1990Sonrasi = (df[(df["hasta_no"] != 0) & (df["dogum_tarihi"] >= "1990-01-01")]
                            .drop(columns=["personel_no","departman","maas","uzmanlik","deneyim_yili","hastane","calisma_saati","sertifika",]))
        print(f"Dogum tarihi 1990 ve sonrası olan hastalar;\n{hasta1990Sonrasi}")

        print("\n*******************************************************\n")

        #Var olan DataFrame'den ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastalik, tedavi bilgilerini
        #içeren yeni bir DataFrame elde edildi ve yazdırıldı
        yeniDf = df[["ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastalik", "tedavi"]]
        print(f"ad, soyad, departman, maas, uzmanlik, deneyim yili, hastalik ve tedavi bilgileri iceren yeni DataFrame;\n{yeniDf}")

    except Exception as e:
        print(f"-*- HATA! HATA! HATA! -*- \n{e}")

if __name__ == "__main__":
    main()
