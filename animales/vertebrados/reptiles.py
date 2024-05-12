from animales.vertebrados.vertebrados import Vertebrados


class Reptiles(Vertebrados):
    def __init__(self, color, tipo_sangre, habitad, alimentacion, num_vertebras, ojos, patas, voca, nombre_cientifico, tipo_piel, edad):
        super().__init__(color=color,
                         tipo_sangre=tipo_sangre,
                         habitad=habitad,
                         alimentacion=alimentacion,
                         num_vertebras=num_vertebras,
                         ojos=ojos,
                         patas=patas,
                         voca=voca,
                         nombre_cientifico=nombre_cientifico,
                         tipo_piel=tipo_piel,
                         edad=edad)
        self.color = color
        self.tipo_sangre = tipo_sangre
        self.habitad = habitad
        self.alimentacion = alimentacion

    def puedo_nadar(self):
        print("Puedo nadar")
    def mudo_de_piel(self):
        print("Mudo de piel cuando crezco")
    def huevo(self):
        print("Nazco de huevo")
