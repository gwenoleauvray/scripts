# ai/ocr_ai.py

Lit le texte d'une image (photo de document, capture d'écran). Trois modes :

| Mode | Commande | Ce qui sort de la machine |
|---|---|---|
| Tesseract seul | `ocr_ai.py image.png` | Rien, 100 % local. |
| Tesseract + correction IA | `ocr_ai.py image.png --clean` | Le **texte** lu est envoyé à l'API Anthropic. |
| Lecture par l'IA | `ocr_ai.py image.png --vision` | L'**image** est envoyée à l'API Anthropic. |

## Prérequis

- Tesseract installé : [`installPyTesseract`](installPyTesseract.md).
- Les modules Python :

```bash
python3 -m venv ~/.venvs/ai && ~/.venvs/ai/bin/pip install -r ai/requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."     # seulement pour --clean et --vision
```

## Utilisation

```bash
cd ai
~/.venvs/ai/bin/python ocr_ai.py facture.png
~/.venvs/ai/bin/python ocr_ai.py facture.png --clean
~/.venvs/ai/bin/python ocr_ai.py facture.png --vision > facture.txt   # enregistre le texte
```

## Options

| Option | Effet |
|---|---|
| `--lang` | Langues de Tesseract (défaut : `fra+eng`). Exemple : `--lang eng`. |
| `--clean` | Claude corrige les erreurs de lecture, sans rien ajouter ni résumer. |
| `--vision` | Claude lit l'image lui-même. Souvent meilleur sur les photos difficiles. |
| `--model NOM` | Choisit le modèle Claude. |

Avec `--clean` ou `--vision`, un passage impossible à lire est marqué `[illisible]`.

## Bon à savoir

- En mode `--vision`, une image trop lourde est réduite automatiquement (en mémoire, l'original n'est pas touché) pour respecter la limite de taille de l'API.
- N'envoyez pas de documents confidentiels avec `--clean` ou `--vision` : utilisez le mode local.

## Ce que le script modifie

Rien : il affiche le texte à l'écran.
