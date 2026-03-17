from collections import Counter
import re

class Texte : # document littéraire avec ses métadonnées et des méthodes d'analyses simples 
  genre_par_defaut = "Texte" # attribut de CLASSE

  def __init__ (self, titre: str, auteur: str, contenu: str, annee: int):
    self.titre = titre # attributs d'INSTANCE
    self.auteur = auteur
    self.contenu = contenu
    self.annee = annee
 
  def __str__(self):
    return f'"{self.titre}" de {self.auteur} ({self.annee})'

  def __repr__(self):
    return f"Texte(titre={self.titre!r}, auteur={self.auteur!r}, annee={self.annee!r})"

  def __len__(self):
    return self.nombres_mots()

  def __contains__(self, mot):
    return mot.lower() in self.contenu.lower()

  def __eq__(self, other):
    if not isinsistance(other, Texte):
      return NotImplemented
    return (self.titre, self.auteur, self.annee) == (other.titre, other.auteur, other.annee)

  def __add__(self, other):
    if not isinsistance(other, Texte):
      return NotImplemented
    return Texte(
      f"{self.titre} + {other.titre}",
      self.auteur,
      self.contenu + " " + other.contenu,
      max(self.annee, other.annee)
      )

  def __iter__(self):
    return iter(self.contenu.split())

  def nombres_mots(self):
    return len(self.contenu.split())
  
  @property
  def titre (self) -> str :
    return self._titre
    
  @titre.setter
  def titre (self, nouveau: str) -> None :
    if not nouveau.strip () :
      raise ValueError ("Le titre ne peut pas etre vide")
    self._titre = nouveau.strip()

def __lt__(self, other):
  if not isinsistance(other, Texte):
    return NotImplemented
  return self.annee < other.annee

andros = Texte("The woman of andros", "Wilder", "The earth sighed as it turned in its course; the shadow of night crept gradually along the Mediterranean, and Asia was left in darkness.", 1930)

print(andros.nombres_mots())
print(andros)        # __str__
len(andros)          # __len__
"earth" in andros    # __contains__


# old version

from collections import Counter
import re

class Texte : # document littéraire avec ses métadonnées et des méthodes d'analyses simples 
  genre_par_defaut = "Texte" # attribut de CLASSE
  def __init__ (self, titre: str, auteur: str, contenu: str, annee: int):
    self.titre = titre # attributs d'INSTANCE
    self.auteur = auteur
    self.contenu = contenu
    self.annee = annee
 
  def nombres_mots(self) -> int :
    return sum (len(c.split()) for c in self.contenu)
  
  def mots_uniques(self) -> set[str] : 
    counter = Counter(self.contenu.lower().split())
    return {mot for mot in counter if counter[mot] == 1}

  
  def frequence(self) -> dict[str, int] :
    words = re.findall(r'\w+', open('texte02.txt').read().lower())
    Counter(words).most_common()
    return {mot: self.contenu.count(mot) for mot in set (self.contenu.split())}
    
  @property
  def titre (self) -> str :
    return self._titre
    
  @titre.setter
  def titre (self, nouveau: str) -> None :
    if not nouveau.strip () :
      raise ValueError ("Le titre ne peut pas etre vide")
    self._titre = nouveau.strip()

andros = Texte("The woman of andros", "Wilder", "The earth sighed as it turned in its course; the shadow of night crept gradually along the Mediterranean, and Asia was left in darkness.", 1930)

print(andros.nombres_mots())
print(andros.mots_uniques())
print(andros.frequence())
print(andros.genre_par_defaut)