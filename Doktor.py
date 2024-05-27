import Personel
class Doktor(Personel.Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.uzmanlik = uzmanlik
        self.deneyim_yili = deneyim_yili
        self.hastane = hastane

    def getUzmanlik(self):
        return self.uzmanlik

    def getDeneyimYili(self):
        return self.deneyim_yili

    def getHastane(self):
        return self.hastane

    def setUzmanlik(self, uzmanlik):
        self.uzmanlik = uzmanlik

    def setDeneyimYili(self, deneyimYili):
        self.deneyim_yili = deneyimYili

    def setHastane(self, hastane):
        self.hastane = hastane

    def maasArttir(self):
        self.maas = int(self.maas*1.2)

    def __str__(self):
        return f"Doktor;\n{super().__str__()}\n Uzmanlik: {self.uzmanlik}\n Deneyim Yili: {self.deneyim_yili}\n Hastane: {self.hastane}"

