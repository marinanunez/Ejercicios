class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero.")
        self._radio = radio
