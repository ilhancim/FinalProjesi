class Personel():
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.personel_no = personel_no
        self.ad = ad
        self.soyad = soyad
        self.departman = departman
        self.maas = maas

    #Get metodları eklendi
    def getPersonelNo(self):
        return self.personel_no

    def getAd(self):
        return self.ad

    def getSoyad(self):
        return self.soyad

    def getDepartman(self):
        return self.departman

    def getMaas(self):
        return self.maas

    #Set metodları eklendi
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

    #Str metodu eklendi
    def __str__(self):
        return (f"{self.personel_no} {self.ad} {self.soyad} {self.departman} {self.maas} ")
