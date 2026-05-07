# outils_console.py
# ================================================
# OUTILS AVANCÉS POUR L'AFFICHAGE DANS LA CONSOLE
# ================================================
# Tout est en français : noms de variables, fonctions, commentaires et docstrings.
# Compatible Linux, macOS et Windows 10+ (codes ANSI).
# 
# Utilisation dans ton programme principal :
#    from outils_console import OutilsConsole, initialiser_console
# ================================================

import sys
import os
from typing import Optional


class OutilsConsole:
    """Classe principale pour contrôler l'affichage dans la console en temps réel.
    
    Tout est fait avec des codes ANSI + flush() pour éviter les bugs d'affichage.
    Idéal pour les animations, les mises à jour en direct, les barres de progression, etc.
    """

    # ================== COULEURS ==================
    COULEURS_TEXTE = {
        'noir': 30, 'rouge': 31, 'vert': 32, 'jaune': 33,
        'bleu': 34, 'magenta': 35, 'cyan': 36, 'blanc': 37,
        'gris_fonce': 90, 'rouge_clair': 91, 'vert_clair': 92,
        'jaune_clair': 93, 'bleu_clair': 94, 'magenta_clair': 95,
        'cyan_clair': 96, 'blanc_clair': 97,
    }

    COULEURS_FOND = {nom: code + 10 for nom, code in COULEURS_TEXTE.items()}

    # ================== CODES ANSI DE BASE ==================
    REINITIALISER_TOUT = "\033[0m"          # Remet tout à zéro (couleurs, styles)
    EFFACER_ECRAN = "\033[2J"               # Efface tout l'écran
    RETOUR_DEBUT = "\033[H"                 # Retour en haut à gauche (0,0)
    EFFACER_LIGNE = "\033[2K"               # Efface uniquement la ligne courante
    CACHER_CURSEUR = "\033[?25l"
    AFFICHER_CURSEUR = "\033[?25h"
    SAUVEGARDER_POSITION = "\033[s"
    RESTAURER_POSITION = "\033[u"

    @staticmethod
    def forcer_affichage():
        """Force l'affichage immédiat (INDISPENSABLE pour les animations en temps réel)."""
        sys.stdout.flush()

    @staticmethod
    def effacer_ecran():
        """Efface complètement l'écran et repositionne le curseur en haut à gauche."""
        print(OutilsConsole.EFFACER_ECRAN + OutilsConsole.RETOUR_DEBUT, end='')
        OutilsConsole.forcer_affichage()

    @staticmethod
    def reinitialiser():
        """Réinitialise toutes les couleurs et styles."""
        print(OutilsConsole.REINITIALISER_TOUT, end='')
        OutilsConsole.forcer_affichage()

    @staticmethod
    def deplacer_curseur(ligne: int, colonne: int):
        """Déplace le curseur à la position exacte (ligne, colonne).
        
        Les positions commencent à 0 (ligne 0 = tout en haut).
        Exemple : deplacer_curseur(5, 10) → ligne 5, colonne 10.
        """
        print(f"\033[{ligne + 1};{colonne + 1}H", end='')
        OutilsConsole.forcer_affichage()

    @staticmethod
    def ecrire_a_position(ligne: int, colonne: int, texte: str, 
                          couleur_texte: str = None, 
                          couleur_fond: str = None, 
                          reinitialiser: bool = True):
        """Écrit du texte à un endroit précis de l'écran.
        
        Parfait pour les mises à jour en temps réel sans bug.
        Exemple : OutilsConsole.ecrire_a_position(3, 5, "✅ OK", couleur_texte="vert_clair")
        """
        OutilsConsole.deplacer_curseur(ligne, colonne)
        
        if couleur_texte and couleur_texte in OutilsConsole.COULEURS_TEXTE:
            print(f"\033[{OutilsConsole.COULEURS_TEXTE[couleur_texte]}m", end='')
        
        if couleur_fond and couleur_fond in OutilsConsole.COULEURS_FOND:
            print(f"\033[{OutilsConsole.COULEURS_FOND[couleur_fond]}m", end='')
        
        print(texte, end='')
        
        if reinitialiser:
            OutilsConsole.reinitialiser()
        
        OutilsConsole.forcer_affichage()

    @staticmethod
    def definir_couleur_texte(couleur: str):
        """Change la couleur du texte (reste actif jusqu'au prochain reinitialiser)."""
        if couleur in OutilsConsole.COULEURS_TEXTE:
            print(f"\033[{OutilsConsole.COULEURS_TEXTE[couleur]}m", end='')
            OutilsConsole.forcer_affichage()

    @staticmethod
    def definir_couleur_fond(couleur: str):
        """Change la couleur de fond (reste actif jusqu'au prochain reinitialiser)."""
        if couleur in OutilsConsole.COULEURS_FOND:
            print(f"\033[{OutilsConsole.COULEURS_FOND[couleur]}m", end='')
            OutilsConsole.forcer_affichage()

    @staticmethod
    def cacher_curseur():
        """Cache le curseur (très utile pendant les animations)."""
        print(OutilsConsole.CACHER_CURSEUR, end='')
        OutilsConsole.forcer_affichage()

    @staticmethod
    def afficher_curseur():
        """Rend le curseur visible à nouveau."""
        print(OutilsConsole.AFFICHER_CURSEUR, end='')
        OutilsConsole.forcer_affichage()

    @staticmethod
    def effacer_ligne():
        """Efface uniquement la ligne où se trouve le curseur."""
        print(OutilsConsole.EFFACER_LIGNE, end='')
        OutilsConsole.forcer_affichage()

    @staticmethod
    def ecraser_ligne(texte: str, couleur_texte: str = None, couleur_fond: str = None):
        """Écrase complètement la ligne courante (idéal pour les barres de progression)."""
        OutilsConsole.effacer_ligne()
        if couleur_texte:
            OutilsConsole.definir_couleur_texte(couleur_texte)
        if couleur_fond:
            OutilsConsole.definir_couleur_fond(couleur_fond)
        print(texte, end='')
        OutilsConsole.reinitialiser()
        OutilsConsole.forcer_affichage()

    @staticmethod
    def sauvegarder_position():
        """Sauvegarde la position actuelle du curseur."""
        print(OutilsConsole.SAUVEGARDER_POSITION, end='')
        OutilsConsole.forcer_affichage()

    @staticmethod
    def restaurer_position():
        """Revient à la position sauvegardée précédemment."""
        print(OutilsConsole.RESTAURER_POSITION, end='')
        OutilsConsole.forcer_affichage()


# ================== INITIALISATION (surtout pour Windows) ==================
def initialiser_console():
    """À appeler UNE SEULE FOIS au début de ton programme.
    
    Active les couleurs ANSI sur Windows et prépare la console.
    """
    if os.name == 'nt':  # Windows
        try:
            from colorama import init as init_colorama
            init_colorama(autoreset=True)
            print("✅ Colorama activé pour Windows")
        except ImportError:
            print("⚠️  Astuce : tape 'pip install colorama' pour un meilleur support sur Windows")
    
    OutilsConsole.effacer_ecran()  # Commence avec un écran propre