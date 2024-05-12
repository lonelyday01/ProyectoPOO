from vertebrados import Vertebrados


class Anfibios(Vertebrados):
    def __init__(self, num_vertebras, ojos, patas, voca, baba, nombre_cientifico, tipo_piel, edad, dieta, color):
        super().__init__(ojos=ojos,
                         patas=patas,
                         voca=voca,
                         nombre_cientifico=nombre_cientifico,
                         tipo_piel=tipo_piel,
                         edad=edad,
                         num_vertebras=num_vertebras)
        self.baba = baba
        self.dieta = dieta
        self.color = color

    def comer(self):
        print("la tengo grande, la lengua...")

    def dormir(self):
        print("ZZZ")

    def reproducirse(self):
        print("Oh me vengo")


class Ranas(Anfibios):
    def __init__(self, num_vertebras, ojos, patas, voca, baba, nombre_cientifico, tipo_piel, edad, dieta, color):
        super().__init__(ojos=ojos,
                         patas=patas,
                         voca=voca,
                         nombre_cientifico=nombre_cientifico,
                         tipo_piel=tipo_piel,
                         edad=edad,
                         num_vertebras=num_vertebras,
                         baba=baba,
                         dieta=dieta,
                         color=color)

    def saltar(self):
        print("puedo saltar")

    def emitir_sonido(self):
        print("croac")
