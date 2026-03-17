class AnalyseurFrequences:
    """analyse"""
    def analyser(self, texte): 
        return texte.frequences()

class Exportateur:
    """exporte"""
    def exporter_hmtl(self, texte):
        return f"<h1>{texte.titre}</h1><p>{texte.contenu}</p>"

    def exporter_csv(self, texte):
        return "\n".join(f"{m}, {c}" for m, c in texte.frequences().items())

class Sauvegarder(Exportateur):
    """sauvegarde"""
    def sauvegarder(self, chemin, texte):
        with open(chemin, "w") as f:
            f.write(texte.contenu)
