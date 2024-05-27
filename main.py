import Personel
import Doktor
import Hemsire
import Hasta

personel1 = Personel.Personel(1,"İlhan","Kilic","Bashekim",40000)
personel2 = Personel.Personel(2,"Renas","Tas","Başhekim Yardimcisi",30000)

doktor1 = Doktor.Doktor(3,"Ahmet Mirza","Millet","Göz",20000,"Goz",20,"Cigli Egitim ve Arastirma Hastanesi")
doktor2 = Doktor.Doktor(4,"Muhammed Can","Arica","Genel Cerrahi",18000,"Genel Cerrahi",15,"Cigli Egitim Hastanesi")
doktor3 = Doktor.Doktor(5,"Eda","Karakoc", "Fizik Tedavi",17000,"Fizyoterapist",12,"Cigli Egitim Hastanesi")

hemsire1 = Hemsire.Hemsire(6,"Mehmet Emirhan","Oguz","Acil",11000,10,"Yok","Cigli Egitim ve Arastirma Hastanesi")
hemsire2 = Hemsire.Hemsire(7,"Secil","Tas","Acil",9000,11,"Yok","Cigli Egitim ve Arastirma Hastanesi")
hemsire3 = Hemsire.Hemsire(8,"Muhammet Faik","Duman","Ameliyathane",12000,12,"Yok","Cigli Egitim ve Arastirma Hastanesi")

hasta1 = Hasta.Hasta(1,"Semih","Ertan","06.02.2004","Kol kirik","Alci")
hasta2 = Hasta.Hasta(2,"Mehmet Akif","Duman","26.09.2004","Miyopi","Gozluk")
hasta3 = Hasta.Hasta(3,"İrem","Bagcivan","07.12.2004","Kizamik","Krem")

print(personel1)
print("*****")
print(personel2)
print("*****")
print(doktor1)
print("*****")
print(doktor2)
print("*****")
print(doktor3)
print("*****")
print(hemsire1)
print("*****")
print(hemsire2)
print("*****")
print(hemsire3)
print("***********")
print(hasta1)
print("*****")
print(hasta2)
print("*****")
print(hasta3)
