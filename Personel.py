class Personel():
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.personel_no = personel_no
        self.ad = ad
        self.soyad = soyad
        self.departman = departman
        self.maas = maas

    def getPersonelNo(self):
        return personel_no

    def getAd(self):
        return ad

    def getSoyad(self):
        return soyad

    def getDepartman(self):
        return departman

    def getMaas(self):
        return maas

    def setPersonelNo(self, personel_no):
        self.personel_no = personel_no

    def setAd(self, ad):
        self.ad = ad

    def setSoyad(self, soyad):
        self.soyad = soyad

    def setDepartman(self, departman):
        self.departman = departman

    def setMaas(self, maas):
        self.maas = maas

    def __str__(self):
        return (f" Personel No: {self.personel_no}\n Ad: {self.ad}\n Soyad: {self.soyad}\n"
                f" Departman: {self.departman}\n Maas: {self.maas} ")
