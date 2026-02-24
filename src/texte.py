class Texte : # document littéraire avec ses métadonnées et des méthodes d'analyses simples 
  genre_par_defaut = "Texte" # attribut de CLASSE
  def __init__ (self, titre: str, auteur: str, contenu: str, annee: int):
    self.titre = titre # attributs d'INSTANCE
    self.auteur = auteur
    self.contenu = contenu
    self.annee = annee
    self.chapitres : list [str] = []
  def nombres_mots(self) -> int :
    return sum (len(ch.split()) for ch in self.chapitres)
  def mots_uniques(self) -> set[str] : 
  def frequence(self) -> dict[str, int]
  @property
  def titre (self) -> str :
    return self._titre
  @titre.setter
  def titre (self, nouveau: str) -> None :
    if not nouveau.strip () :
      raise ValueError ("Le titre ne peut pas etre vide ")
    self._titre = nouveau.strip()
