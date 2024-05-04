from seres_vivos import SeresVivos


class Plantas(SeresVivos):
    def __init__(self, nombre_cientifico, edad, tipo):
        super().__init__(nombre_cientifico, edad)
        self.tipo = tipo

    def fotosintesis(self):
        print(f"La planta {self.nombre_cientifico} del tipo {self.tipo} esta haciendo fotosintesis")

    def reproducirse(self):
        print("Se esta reproduciendo con esporas")