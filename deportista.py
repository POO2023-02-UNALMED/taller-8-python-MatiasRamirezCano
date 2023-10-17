class Deportista:

    def __init__(self, añosPracticando, deporte = "futbol"):
        self._añosPracticando = añosPracticando
        self._deporte = deporte
    
    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self, deporte):
        self._deporte = deporte
    
    def getAñosPracticando(self):
        return self._añosPracticando
    
    def setAñosPracticando(self, añosPracticando):
        self._añosPracticando = añosPracticando