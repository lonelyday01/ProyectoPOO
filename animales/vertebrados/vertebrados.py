from animales.animales import Animales


class Vertebrados(Animales):
    def __init__(self, num_vertebras, ojos, patas, voca, nombre_cientifico, tipo_piel, edad):
        super().__init__(ojos=ojos,
                         patas=patas,
                         voca=voca,
                         nombre_cientifico=nombre_cientifico,
                         tipo_piel=tipo_piel,
                         edad=edad)
        self.num_vertebras = num_vertebras

    def me_puedo_roper(self):
        print("Me puedo romper :c")
