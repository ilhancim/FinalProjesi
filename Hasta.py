class Hasta():
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.hasta_no = hasta_no
        self.ad = ad
        self.soyad = soyad
        self.dogum_tarihi = dogum_tarihi
        self.hastalik = hastalik
        self.tedavi = tedavi

    def getHastaNo(self):
        return self.hasta_no

    def getAd(self):
        return self.ad

    def getSoyad(self):
        return self.soyad

    def getDogumTarihi(self):
        return self.dogum_tarihi

    def getHastalik(self):
        return self.hastalik

    def getTedavi(self):
        return self.tedavi

    def setHastaNo(self, hasta_no):
        self.hasta_no = hasta_no

    def setAd(self, ad):
        self.ad = ad

    def setSoyad(self, soyad):
        self.soyad = soyad

    def setDogumTarihi(self, dogum_tarihi):
        self.dogum_tarihi = dogum_tarihi

    def setHastalik(self, hastalik):
        self.hastalik = hastalik

    def setTedavi(self, tedavi):
        self.tedavi = tedavi

    def __str__(self):
        return (f"{self.hasta_no} {self.ad} {self.soyad} {self.dogum_tarihi} {self.hastalik} {self.tedavi}")

