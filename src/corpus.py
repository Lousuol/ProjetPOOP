from export import Exportateur


class Index:
    def __init__(self, exportateur: Exportateur):
        self._entrees: dict[str, list[int]] = {}
    def ajouter(self, mot: str, page: int) -> None:
        self._entrees.setdefault(mot, []).append(page)
    def chercher(self, mot: str) -> list[int]:
        return self._entrees.get(mot, [])
class TableDesMatieres:
    def __init__(self):
        self._chapitres: list[tuple[str, int]] = []
    def ajouter(self, titre: str, page: int) -> None:
        self._chapitres.append((titre, page))
class Livre:
    def __init__(self, titre: str, auteur: str):
        self.titre = titre
        self.auteur = auteur
        self.tdm = TableDesMatieres()  # composition
        self.index = Index()            # composition
    def chercher_mot(self, mot: str) -> list[int]:
        return self.index.chercher(mot)  # delegation
