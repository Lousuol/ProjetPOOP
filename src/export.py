from abc import ABC, abstractmethod

from texte import Texte


class Exportateur(ABC):
    @abstractmethod
    def exporter(texte: Texte) -> str: ...


class ExportateurHTML(Exportateur):
    """exportehtml"""
    def exporter_hmtl(texte: Texte) -> str:
        return f"<h1>{texte.titre}</h1><p>{texte.contenu}</p>"

class ExportateurCSV(Exportateur):
    """exportcsv"""
    def exporter_csv(texte: Texte) -> str:
        return "\n".join(f"{m}, {c}" for m, c in texte.frequences().items())

