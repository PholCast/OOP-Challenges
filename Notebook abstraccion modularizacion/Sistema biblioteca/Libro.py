from dataclasses import dataclass

@dataclass
class Libro:
    titulo: str
    genero: str
    isbn: str
    autor: str
    reservado: bool