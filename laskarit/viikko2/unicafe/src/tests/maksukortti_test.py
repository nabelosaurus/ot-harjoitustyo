import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 15)

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_palautusarvo_oikein_jos_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

    def test_palautusarvo_oikein_jos_rahat_ei_riitta(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)

