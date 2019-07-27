import time
import random
import sys


class Araba():
    __model = 2010
    __vites = "Manuel"

    def __init__(self, isim, motor, beygir_gucu):
        self.isim = isim
        self.motor = motor
        self.beygir_gucu = beygir_gucu
        self.hiz = 140

    def max_hiz(self):
        if self.motor > 1.6:
            if self.beygir_gucu > 106:
                hiz = 250
                return hiz
        else:
            hiz = 200
            return hiz

    def araba_ozellikler(self):
        print(
        "Arabanizin ozellikleri:\n", "Adi: ", self.isim, "\n", "Model: ", self.__model, "\n", "Vites: ", self.__vites,
        "\n",
        "Motor: ", self.motor, "\n", "Beygir Gucu: ", self.beygir_gucu, "\n", "Max hizi: ", self.max_hiz())

    def basla(self):
        print("Evet oyun basliyor....")
        time.sleep(2)
        for i in range(3):
            time.sleep(1)
            print(3 - i, flush=True)
        print('GO!!!!!\n')
        time.sleep(0.2)
        print("                         {}".format(self.isim), flush=True)
        print("                    -----------", flush=True)
        print("           ...      O         O\n", flush=True)

    def yol(self):
        return random.randint(1, 2)

    @classmethod
    def model_artir(cls):
        cls.__model += 1

    def oyundan_cik(self):
        print("Yanlis yol, kaza yaptiniz\n")
        time.sleep(0.4)
        print("                    O         O", flush=True)
        print("                    -----------", flush=True)
        print("                       {}".format(arac.isim), flush=True)
        print('Çıkılıyor...')
        sys.exit()


arac = Araba("Audi", 1.3, 106)
arac.araba_ozellikler()
arac.basla()

hamle = int(input('Sagdaki yol icin 1,sol icin 2 seciniz:\n>'))

if hamle == arac.yol():
    Araba.model_artir()
    print("Tebrikler aracinizin modeli 1 artti")
    arac.araba_ozellikler()
else:
    arac.oyundan_cik()
