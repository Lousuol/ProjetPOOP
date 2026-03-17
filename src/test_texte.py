from exceptions import TexteVideError, AnalyseurError
from texte import Texte


try:
    Texte ("T", "A", "", 1900)
except TexteVideError as e:
    print(f"Erreur : {e}")
    print(f"Titre cherche : {e.titre}")
except AnalyseurError:
    print("Autre erreur de corpus")