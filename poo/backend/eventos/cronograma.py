from datetime import datetime
from typing import List

from .event import Eventos
from .palestrantes import Palestrante


class Cronograma:
    def __init__(self, eventos: List[Eventos], palestrantes: List[Palestrante], horario: datetime):
        self.eventos = eventos
        self.palestrantes = palestrantes
        self.horario = horario

    @classmethod
    def create_cronograma(
        cls,
        eventos: List[Eventos],
        palestrantes: List[Palestrante],
        horario: datetime,
    ) -> "Cronograma":
        return cls(eventos=eventos, palestrantes=palestrantes, horario=horario)

