from dataclasses import dataclass

@dataclass
class Libro:
    titulo: str
    autor: str
    isbn: str
    reservado: bool