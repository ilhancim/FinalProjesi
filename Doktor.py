import Personel
class Doktor(Personel.Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.uzmanlik = uzmanlik
        self.deneyim_yili = deneyim_yili
        self.hastane = hastane

    #Get metodları eklendi
    def getUzmanlik(self):
        return self.uzmanlik

    def getDeneyimYili(self):
        return self.deneyim_yili

    def getHastane(self):
        return self.hastane

    #Set metodları eklendi
    def setUzmanlik(self, uzmanlik):
        self.uzmanlik = uzmanlik

    def setDeneyimYili(self, deneyimYili):
        self.deneyim_yili = deneyimYili

    def setHastane(self, hastane):
        self.hastane = hastane

    #maası 1.2 katına eşitleyen maasArttir metodu eklendi
    def maasArttir(self):
        self.maas = int(self.maas*1.2)

    #Str metodu eklendi
    def __str__(self):
        return f"{super().__str__()} {self.uzmanlik} {self.deneyim_yili} {self.hastane}"

