from Animals import Animal
class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu,):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.paruh = paruh
        self.warna_bulu = warna_bulu
        
    def info_burung(self):
        super().info_animal()
        print('Paruh \t\t\t :', self.paruh,
          '\nWarna Bulu \t\t :', self.warna_bulu)
    
burung_beo = Burung('Beo', 'Biji-bijian', 'udara', 'bertelur', 'melengkung', 'warna-warni')
burung_beo.info_burung()
print('============================================')
burung_merpati = Burung('merpati', 'Beras & Jagung', 'udara', 'bertelur', 'lurus', 'kelabu')
burung_merpati.info_burung()
print('============================================')
burung_murai = Burung('murai batu', 'biji- biji', 'kandang', 'bertelur', 'lurus', 'merah hotam')
burung_murai.info_burung()
