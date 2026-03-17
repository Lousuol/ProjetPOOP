

class AnalyseurError(Exception):
    """exception de base pour les operations sur un corpus."""

class TexteVideError(AnalyseurError):
    pass

class FormatInconnuError(AnalyseurError): 
    pass