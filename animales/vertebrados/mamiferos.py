from vertebrados import Vertebrados


class Mamiferos(Vertebrados):
    def __init__(self, num_vertebras, ojos, patas, voca, nombre_cientifico, tipo_piel, edad, pelaje, glandulas_mamarias, gestacion, tipo_alimentacion):
        super().__init__(ojos=ojos,
                         patas=patas,
                         voca=voca,
                         nombre_cientifico=nombre_cientifico,
                         tipo_piel=tipo_piel,
                         edad=edad,
                         num_vertebras=num_vertebras)
        self.pelaje = pelaje
        self.glandulas_mamarias = glandulas_mamarias
        self.gestacion = gestacion
        self.tipo_alimentacion = tipo_alimentacion

    def amamantar(self):
        print("estoy amamantando")

    def gestacion(self):
        print("estoy gestando")

    def respirar(self):
        print('estoy respirando con pulmones')

    def viven(self):
        print('vivo en manada')
