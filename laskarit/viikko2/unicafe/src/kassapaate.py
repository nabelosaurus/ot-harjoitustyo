class Kassapaate:
    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    def kasvata_myyntilukua(self, hinta):
        if hinta == 240:
            self.edulliset += 1
        if hinta == 400:
            self.maukkaat += 1

    def syo_kateisella(self, maksu, hinta):
        if maksu >= hinta:
            self.kassassa_rahaa = self.kassassa_rahaa + hinta
            self.kasvata_myyntilukua(hinta)
            return maksu - hinta
        else:
            return maksu

    def syo_edullisesti_kateisella(self, maksu):
        return self.syo_kateisella(maksu, 240)

    def syo_maukkaasti_kateisella(self, maksu):
        return self.syo_kateisella(maksu, 400)

    def syo_kortilla(self, kortti, hinta):
        if kortti.saldo >= hinta:
            kortti.ota_rahaa(hinta)
            self.kasvata_myyntilukua(hinta)
            return True
        return False

    def syo_edullisesti_kortilla(self, kortti):
        return self.syo_kortilla(kortti, 240)

    def syo_maukkaasti_kortilla(self, kortti):
        return self.syo_kortilla(kortti, 400)

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        else:
            return
