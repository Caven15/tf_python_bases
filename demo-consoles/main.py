# main.py
from outils_console import OutilsConsole, initialiser_console
import time

# Initialisation obligatoire au début
initialiser_console()
OutilsConsole.cacher_curseur()   # Cache le curseur pour un rendu plus propre

# Exemple 1 : écrire à un endroit précis
OutilsConsole.ecrire_a_position(3, 5, "✅ Tout fonctionne !", couleur_texte="vert_clair")

# Exemple 2 : animation en temps réel SANS bug
try:
    position_x = 10
    while True:
        # Efface l'ancien caractère
        OutilsConsole.ecrire_a_position(10, position_x, "  ")
        
        # Déplace et affiche le nouveau
        position_x = (position_x + 1) % 60
        OutilsConsole.ecrire_a_position(10, position_x, "🚀", couleur_texte="cyan_clair")
        
        time.sleep(0.08)   # Vitesse de l'animation
except KeyboardInterrupt:
    # Arrêt propre quand tu appuies sur Ctrl+C
    OutilsConsole.effacer_ecran()
    OutilsConsole.afficher_curseur()
    print("Programme arrêté proprement ✅")