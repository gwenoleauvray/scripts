# configPyautogui.py

Vérifie que **PyAutoGUI** fonctionne, affiche les informations utiles pour écrire un script (taille de l'écran, position de la souris, réglages), et propose deux petits essais.

*Remplace l'ancien brouillon `configPyautogui`, qui ne fonctionnait pas.*

## Prérequis

- PyAutoGUI installé avec [`installPyautogui`](installPyautogui.md).
- Une session graphique **X11** (le script prévient si vous êtes sous Wayland).

## Utilisation

```bash
PY=~/.venvs/pyautogui/bin/python

$PY configPyautogui.py                       # affiche l'état
$PY configPyautogui.py --test                # la souris dessine un carré
$PY configPyautogui.py --ecrire "Bonjour"    # tape un texte après 5 secondes
$PY configPyautogui.py --pause 0.3 --test    # essai plus lent
```

## Options

| Option | Effet |
|---|---|
| *(aucune)* | Affiche Python, PyAutoGUI, type de session, taille de l'écran, position de la souris, FAILSAFE et pause. |
| `--test` | Après 3 secondes, déplace la souris en carré de 100 pixels autour de sa position, puis la remet en place. |
| `--ecrire TEXTE` | Après 5 secondes (le temps de cliquer dans une fenêtre), tape le texte. |
| `--pause S` | Pause en secondes entre deux actions de PyAutoGUI (défaut 0.1). |

Forme de l'affichage (les valeurs dépendent de votre machine) :

```
Python        : 3.x.y
PyAutoGUI     : a.b.c
Session       : x11
Écran         : 1920 x 1080 pixels
Souris        : X=812  Y=455
FAILSAFE      : activé (souris dans un coin = arrêt)
Pause         : 0.1 s entre deux actions
```

## Sécurité : l'arrêt d'urgence

Le script active toujours **FAILSAFE** : envoyer brusquement la souris dans **un coin de l'écran** arrête tout. Le carré de `--test` reste à distance des bords pour ne pas le déclencher par erreur. **Ctrl-C** arrête aussi le script.

## Bon à savoir

- `--ecrire` tape les caractères comme sur un clavier anglais : les **lettres accentuées** peuvent ne pas sortir, selon la configuration du clavier.
- Les mêmes réglages s'utilisent dans vos propres scripts :

```python
import pyautogui
pyautogui.FAILSAFE = True   # garder l'arrêt d'urgence
pyautogui.PAUSE = 0.2       # pause entre deux actions
```

## Ce que le script modifie

Rien sur la machine. Avec `--test` ou `--ecrire`, il bouge la souris ou tape au clavier, comme demandé.
