class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero.")
        self._radio = radio

def radio(self):
    return self._radio

def radio(self, valor):
    if valor <= 0:
        raise ValueError("El radio debe ser mayor que cero.")
    self._radio = valor