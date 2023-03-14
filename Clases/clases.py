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
    
def area(self):
    return 2 * 3.14159 * self._radio

def __repr__(self):
    return f"Circulo de radio {self._radio}"

def __mul__(self, n):
    if n <= 0:
        raise ValueError("El factor de multiplicación debe ser mayor que cero.")
    return Circulo(self._radio * n) 