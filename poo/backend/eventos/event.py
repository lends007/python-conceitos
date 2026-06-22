from datetime import datetime
from typing import List, Optional

from .palestrantes import Palestrante
from .user import User


class Event:
    def __init__(
        self,
        title: str,
        description: str,
        date: datetime,
        regra: str = "",
        location: str = "",
        user: Optional[User] = None,
    ):
        self.title = title
        self.description = description
        self.date = date
        self.regra = regra
        self.location = location
        self.user = user

    def __repr__(self) -> str:
        return (
            f"{self.title}\n"
            f"{self.description}\n"
            f"{self.date}\n"
            f"{self.location}\n"
            f"{self.user}"
        )

    @classmethod
    def create_event(cls, data: dict) -> "Event":
        # Mantém simples: pega valores do dict
        return cls(
            title=data["title"],
            description=data.get("description", ""),
            date=data["date"],
            regra=data.get("regra", ""),
            location=data.get("location", ""),
            user=data.get("user"),
        )


class Eventos:
    def __init__(self):
        self.palestrantes: List[Palestrante] = []

    def adicionar_palestrante(self, palestrante: Palestrante) -> None:
        self.palestrantes.append(palestrante)

    def adicionar_varios_palestrantes(self, palestrantes: List[Palestrante]) -> None:
        self.palestrantes.extend(palestrantes)

