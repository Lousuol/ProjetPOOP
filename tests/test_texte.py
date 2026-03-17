from ..src.exceptions import TexteVideError, AnalyseurError
from ..src.texte import Texte


try:
    Texte ("T", "A", "")
except TexteVideError as e:
    print(f"Erreur : {e}")
except AnalyseurError:
    print("Autre erreur de corpus")