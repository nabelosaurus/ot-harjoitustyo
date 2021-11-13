import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.tuhat_euroa_sentteina = 1000 * 100

    def test_kassapaate_aloitussaldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.tuhat_euroa_sentteina)

    def test_kassapaate_myynnit_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_toimii_oikein_jos_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 260)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kateisella_toimii_oikein_jos_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_riittamaton_maksu_kateisella_toimii_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0) #

    def test_maukas_riittamaton_maksu_kateisella_toimii_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0) #

    def test_syo_edullisesti_kortilla_toimii_oikein_jos_kortilla_saldoa(self):
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(vastaus)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 1000-240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kortilla_toimii_oikein_jos_kortilla_saldoa(self):
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(vastaus)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 1000-400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kortilla_toimii_oikein_jos_kortilla_ei_ole_saldoa(self):
        self.maksukortti.saldo = 200
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertFalse(vastaus)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_toimii_oikein_jos_kortilla_ei_ole_saldoa(self):
        self.maksukortti.saldo = 200
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertFalse(vastaus)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_arvon_lataaminen_kortille_toimii_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_negatiivisen_arvon_lataaminen_kortille_toimii_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 1000)