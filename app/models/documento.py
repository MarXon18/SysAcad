from dataclasses import dataclass  

@dataclass(init=False, repr=True, eq=True)
class Documento:
    id: int
    tipo_documento: str