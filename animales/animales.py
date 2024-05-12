from seres_vivos import SeresVivos


class Animales(SeresVivos):
    def __init__(self, patas, ojos, voca, tipo_piel, nombre_cientifico, edad):
        super().__init__(nombre_cientifico=nombre_cientifico, edad=edad)
        self.patas = patas
        self.ojos = ojos
        self.voca = voca
        self.tipo_piel = tipo_piel

    def comer(self):
        print("puedo comer")

    def dormir(self):
        print("Estoy durmiendo")

    def reproducirse(self):
        print("Me reproduzco por sexo")