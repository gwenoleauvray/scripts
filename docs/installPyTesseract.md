# installPyTesseract

Installe **Tesseract**, un logiciel libre de reconnaissance de texte (OCR) : il lit le texte présent dans une image ou une photo de document. Installe aussi `pytesseract`, pour l'utiliser depuis Python.

## Prérequis

- Debian ou Ubuntu, avec les droits `sudo`.

## Utilisation

```bash
./installPyTesseract
```

Pour installer dans un autre dossier que `~/.venvs/ocr` :

```bash
VENV=~/mon/dossier ./installPyTesseract
```

## Ce que le script modifie

1. Installe les paquets système `tesseract-ocr`, les langues française (`tesseract-ocr-fra`) et anglaise (`tesseract-ocr-eng`), et de quoi créer un environnement Python.
2. Crée un environnement virtuel dans `~/.venvs/ocr`.
3. Y installe `pillow` (ouvrir les images) et `pytesseract`.
4. Affiche la version de Tesseract pour confirmer que tout marche.

Le script s'arrête à la première erreur.

## Après l'installation

Lire le texte d'une image avec l'outil du dépôt :

```bash
~/.venvs/ocr/bin/python ai/ocr_ai.py mon_image.png
```

Voir le manuel [`ocr_ai`](ocr_ai.md) pour les options avec IA.

Ou directement en ligne de commande :

```bash
tesseract mon_image.png sortie -l fra     # écrit le texte dans sortie.txt
```

## Désinstaller

```bash
rm -rf ~/.venvs/ocr
sudo apt remove tesseract-ocr tesseract-ocr-fra tesseract-ocr-eng
```
