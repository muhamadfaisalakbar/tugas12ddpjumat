from Animals import Animal

class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, habitat, bisa_konsumsi):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.bisa_konsumsi = bisa_konsumsi
    def info_ikan(self):
        super().info_animal()
        print('Habitat \t\t :',self.habitat,
              '\nKonsumsi \t\t :',self.bisa_konsumsi)
        
ikan_nila = Ikan('Nila','Pelet','Air','Bertelur','Tawar','Untuk dikonsumsi')
ikan_nila.info_ikan()
print('============================================')
ikan_hiu = Ikan('Hiu Biru','Ikan Kecil/Cumi','Air','beranak','Air Laut','Tidak untuk dikonsumsi')
ikan_hiu.info_ikan()
print('============================================')
