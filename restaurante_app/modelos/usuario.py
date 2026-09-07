class Usuario:
    def __init__(self, identificacion: str, nombre: str, mesa: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.mesa = mesa

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La identificacion no puede estar vacia.")
        self._identificacion = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre del cliente no puede estar vacio.")
        self._nombre = valor.strip()

    @property
    def mesa(self) -> str:
        return self._mesa

    @mesa.setter
    def mesa(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El numero de mesa no puede estar vacio.")
        self._mesa = valor.strip()

    def convertir_a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "mesa": self.mesa,
        }

    def __str__(self) -> str:
        return (
            f"Identificacion: {self.identificacion} | "
            f"Nombre: {self.nombre} | Mesa: {self.mesa}"
        )
