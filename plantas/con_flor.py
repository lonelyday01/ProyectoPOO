from plantas.plantas import Plantas


class ConFlor(Plantas):
    def __init__(self, nombre_cientifico, edad, tipo, color, nombre_local="hola"):
        super().__init__(nombre_cientifico, edad, tipo)
        self.color = color
        self.nombre_local = nombre_local

    def florear(self):
        print(f"La planta {self.nombre_cientifico} del tipo {self.tipo} conocida como {self.nombre_local} esta floreando")

    def reproducirse(self):
        print("Se esta reproduciendo con esporas")

    def test_function_flake8_rule(self):
        print("funciona")
