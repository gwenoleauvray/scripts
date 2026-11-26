# installPyautogui

Installe **PyAutoGUI**, un module Python qui pilote la souris et le clavier (automatiser des clics, taper du texte, faire des captures d'écran).

## Prérequis

- Debian ou Ubuntu, avec les droits `sudo`.
- Une session graphique **X11**. PyAutoGUI ne fonctionne pas sous Wayland.

## Utilisation

```bash
./installPyautogui
```

Pour installer dans un autre dossier que `~/.venvs/pyautogui` :

```bash
VENV=~/mon/dossier ./installPyautogui
```

## Ce que le script modifie

1. Installe les paquets système `python3`, `python3-venv`, `python3-pip`, `python3-tk`, `python3-dev` et `scrot` (capture d'écran).
2. Crée un **environnement virtuel** dans `~/.venvs/pyautogui`. C'est un dossier Python isolé : Debian 12 et plus récents interdisent d'installer avec pip pour tout le système.
3. Y installe `pyautogui`, `python-xlib` et `pillow`.

Le script s'arrête à la première erreur.

## Après l'installation

```bash
source ~/.venvs/pyautogui/bin/activate      # active l'environnement
python mousePosition.py                      # affiche la position de la souris
deactivate                                   # quitte l'environnement
```

Petit essai :

```python
import pyautogui
pyautogui.moveTo(100, 100)       # déplace la souris
pyautogui.write("Bonjour")       # tape un texte
pyautogui.press("enter")         # appuie sur Entrée
```

## Désinstaller

```bash
rm -rf ~/.venvs/pyautogui
```

Les paquets système peuvent rester, ils servent à d'autres programmes.

## Dépannage

- **Erreur d'affichage ou rien ne bouge** : vérifier qu'on est sous X11 avec `echo $XDG_SESSION_TYPE`. La réponse doit être `x11`.
