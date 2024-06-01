class Hasta():
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.hasta_no = hasta_no
        self.ad = ad
        self.soyad = soyad
        self.dogum_tarihi = dogum_tarihi
        self.hastalik = hastalik
        self.tedavi = tedavi

    #Get metodları eklendi
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

    #Set metodları eklendi
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

    #tedavi girilirken x_yyyy formatında girilir x kısmı(A, B, C, D, E) tedavinin süresi için yyyy kısmı ise tedavi adıdır.
    def tedaviSuresiHesapla(self):
        self.sure = 7
        #ilk harf A ise tedavi süresi 7 gün kalır
        if self.tedavi[0] == "A":
            self.sure = self.sure

        #ilk harf B ise tedavi süresine 2 gün eklenir
        elif self.tedavi[0] == "B":
            self.sure = self.sure + 2

        #ilk harf C ise tedavi süresine 5 gün eklenir
        elif self.tedavi[0] == "C":
            self.sure = self.sure + 5

        #ilk harf D ise tedavi süresine 9 gün eklenir
        elif self.tedavi[0] == "D":
            self.sure = self.sure + 9

        #ilk harf E ise tedavi süresine 14 gün eklenir
        elif self.tedavi[0] == "E":
            self.sure = self.sure + 14

    # Str metodu eklendi
    def __str__(self):
        return (f"{self.hasta_no} {self.ad} {self.soyad} {self.dogum_tarihi} {self.hastalik} {self.tedavi}")

