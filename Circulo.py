
import math
class Circulo:

    def __init__(self, radio):
        self._radio = radio

    def area(self):
        return math.pi*self.radio*self.radio

    def circunferencia(self):
        return 2*self.radio*math.pi