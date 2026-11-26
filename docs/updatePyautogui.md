# updatePyautogui

Met à jour **PyAutoGUI** et ses dépendances (`python-xlib`, `pillow`) dans l'environnement créé par [`installPyautogui`](installPyautogui.md).

*Remplace l'ancien `installPyautoguiOK`.*

## Prérequis

- PyAutoGUI déjà installé avec `installPyautogui`.

## Utilisation

```bash
./updatePyautogui
```

Si l'environnement a été installé ailleurs que dans `~/.venvs/pyautogui` :

```bash
VENV=~/mon/dossier ./updatePyautogui
```

Forme de l'affichage (les numéros dépendent de votre installation) :

```
Avant :
  pyautogui    a.b.c
  python-xlib  a.b
  pillow       a.b.c
Après :
  pyautogui    a.b.c
  python-xlib  a.b
  pillow       x.y.z      <- module mis à jour
No broken requirements found.
OK : PyAutoGUI est à jour.
```

## Ce que le script modifie

Seulement l'environnement virtuel :

1. Met à jour `pip`.
2. Met à jour `pyautogui`, `python-xlib` et `pillow`.
3. Vérifie que les modules installés sont compatibles entre eux (`pip check`).

Il ne demande **pas** `sudo` et ne touche pas aux paquets du système.

## Dépannage

- **« Aucun environnement PyAutoGUI »** : lancer d'abord `./installPyautogui`.
- **Un module ne marche plus après la mise à jour** : revenir à une version précise, en remplaçant `x.y.z` par la version « Avant » affichée : `~/.venvs/pyautogui/bin/pip install pillow==x.y.z`.
