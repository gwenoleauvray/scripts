#!/usr/bin/env python3
"""Vérifie et règle PyAutoGUI : écran, souris, sécurité, essais.

Usage :
  configPyautogui.py                  affiche l'état (écran, souris, réglages)
  configPyautogui.py --test           petit carré de souris pour vérifier que ça marche
  configPyautogui.py --ecrire "Bonjour"   tape un texte après 5 secondes
  configPyautogui.py --pause 0.3 --test   change la pause entre deux actions

Prérequis : PyAutoGUI installé (./installPyautogui), session graphique X11.
Sécurité : envoyer la souris dans un COIN de l'écran arrête tout (FAILSAFE).
Manuel : docs/configPyautogui.md
"""
import argparse
import os
import platform
import sys
import time


def charger_pyautogui():
    """Importe PyAutoGUI avec un message clair si c'est impossible."""
    if os.environ.get("XDG_SESSION_TYPE") == "wayland":
        print("⚠ Session Wayland détectée : PyAutoGUI ne fonctionne que sous X11.")
    try:
        import pyautogui
    except ImportError:
        sys.exit("PyAutoGUI n'est pas installé. Lancer ./installPyautogui, puis\n"
                 "  ~/.venvs/pyautogui/bin/python configPyautogui.py")
    except Exception as erreur:  # pas d'écran (connexion SSH, pas de DISPLAY…)
        sys.exit(f"Impossible d'accéder à l'écran : {erreur}")
    return pyautogui


def compte_a_rebours(secondes, message):
    """Laisse le temps de placer la fenêtre ou de lâcher la souris."""
    print(message)
    for reste in range(secondes, 0, -1):
        print(f"  {reste}…", flush=True)
        time.sleep(1)


def afficher_etat(pag):
    """Affiche les informations utiles pour écrire un script PyAutoGUI."""
    largeur, hauteur = pag.size()
    x, y = pag.position()
    print(f"Python        : {platform.python_version()}")
    print(f"PyAutoGUI     : {pag.__version__}")
    print(f"Session       : {os.environ.get('XDG_SESSION_TYPE', 'inconnue')}")
    print(f"Écran         : {largeur} x {hauteur} pixels")
    print(f"Souris        : X={x}  Y={y}")
    print(f"FAILSAFE      : {'activé' if pag.FAILSAFE else 'DÉSACTIVÉ'} (souris dans un coin = arrêt)")
    print(f"Pause         : {pag.PAUSE} s entre deux actions")


def test_souris(pag, cote=100):
    """Déplace la souris en carré autour de sa position, puis la remet en place."""
    largeur, hauteur = pag.size()
    depart_x, depart_y = pag.position()
    # On garde le carré à au moins 10 pixels des bords (les coins déclenchent FAILSAFE).
    x = min(max(depart_x, 10), largeur - cote - 10)
    y = min(max(depart_y, 10), hauteur - cote - 10)
    compte_a_rebours(3, "Test : la souris va dessiner un carré. Lâchez-la.")
    for px, py in [(x, y), (x + cote, y), (x + cote, y + cote), (x, y + cote), (x, y)]:
        pag.moveTo(px, py, duration=0.3)
    pag.moveTo(depart_x, depart_y, duration=0.3)
    print("OK : la souris a bougé, PyAutoGUI fonctionne.")


def ecrire(pag, texte):
    """Tape un texte dans la fenêtre active, après un délai pour la choisir."""
    compte_a_rebours(5, "Cliquez dans la fenêtre où taper le texte.")
    # write() ne tape que les caractères du clavier anglais : les accents
    # peuvent ne pas sortir selon la configuration du clavier.
    pag.write(texte, interval=0.05)
    print("\nOK : texte tapé.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--test", action="store_true", help="déplace la souris en carré")
    parser.add_argument("--ecrire", metavar="TEXTE", help="tape TEXTE après 5 secondes")
    parser.add_argument("--pause", type=float, metavar="S", help="pause entre deux actions (défaut 0.1)")
    args = parser.parse_args()

    pag = charger_pyautogui()
    pag.FAILSAFE = True  # toujours garder l'arrêt d'urgence
    if args.pause is not None:
        pag.PAUSE = max(0.0, args.pause)

    afficher_etat(pag)
    try:
        if args.test:
            print()
            test_souris(pag)
        if args.ecrire:
            print()
            ecrire(pag, args.ecrire)
    except pag.FailSafeException:
        sys.exit("\nArrêt d'urgence : souris placée dans un coin de l'écran.")
    except KeyboardInterrupt:
        sys.exit("\nInterrompu.")


if __name__ == "__main__":
    main()
