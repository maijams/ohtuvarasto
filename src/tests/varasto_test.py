import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varastook = Varasto(50, 10)
        self.varastohuono = Varasto(-100, -10)
        self.varastotaysi = Varasto(100, 1000)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_konstruktori_nollaa_negatiivisen_alkusaldon(self):
        self.assertAlmostEqual(self.varastohuono.saldo, 0)
        
    def test_konstruktori_alkusaldo_oikein(self):
        self.assertAlmostEqual(self.varastook.saldo, 10)
        
    def test_konstruktori_luo_tayden_varaston(self):
        self.assertAlmostEqual(self.varastotaysi.saldo, 100)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        self.assertAlmostEqual(self.varastohuono.tilavuus, 0)
        
    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
        
    def test_negatiivinen_lisays_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(-10)
        
        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_varasto_tayttyy_lisayksesta(self):
        self.varasto.lisaa_varastoon(100)
        
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)
    
    def test_negatiivinen_ottaminen_palauttaa_nollan(self):
        saatu_maara = self.varasto.ota_varastosta(-10)
        
        self.assertAlmostEqual(saatu_maara, 0)
        
    def test_liian_iso_otto_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(10)
        
        saatu_maara = self.varasto.ota_varastosta(100)
        
        self.assertAlmostEqual(saatu_maara, 10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_kuvaus_toimii(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")