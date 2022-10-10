class Road:
    def __init__(self):
        self._length=0
        self._width=0

    def mass(self,length,width,mas,tol):
        self._length = length
        self._width = width
        return self._width*self._length*mas*tol


ro=Road()
print(f"Масса дорожного полотна: {ro.mass(10,12,4,2)} кг")