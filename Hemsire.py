import Personel
class Hemsire(Personel.Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.calisma_saati = calisma_saati
        self.sertifika = sertifika
        self.hastane = hastane

    def getCalismaSaati(self):
        return self.calisma_saati

    def getSertifika(self):
        return self.sertifika

    def getHastane(self):
        return self.hastane

    def SetCalismaSaati(self, calisma_saati):
        self.calisma_saati = calisma_saati

    def SetSertifika(self, sertifika):
        self.sertifika = sertifika

    def SetHastane(self, hastane):
        self.hastane = hastane

    def maasArttir(self):
        self.maas = int(self.maas*1.2)

    def __str__(self):
        return f"{super().__str__()} {self.calisma_saati} {self.sertifika} {self.hastane}"

