class SeresVivos:
    def __init__(self, nombre_cientifico, edad):
        self.nombre_cientifico = nombre_cientifico
        self.edad = edad

    def reproducirse(self):
        print(f"{self.nombre_cientifico} se esta reproduciendo")

    def viven(self):
        print(f"El animal {self.nombre_cientifico} vive y ha vivido {self.edad} años")
