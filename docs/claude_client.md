# ai/claude_client.py

Brique commune des outils IA du dépôt (`verify_script.py`, `ocr_ai.py`). **Ce fichier ne se lance pas seul** : il fournit une fonction `ask()` qui envoie une demande à Claude et renvoie sa réponse.

## Réglages

| Variable d'environnement | Rôle |
|---|---|
| `ANTHROPIC_API_KEY` | Clé API, obligatoire. À créer sur https://console.anthropic.com/. |
| `ANTHROPIC_MODEL` | Modèle à utiliser. Défaut : `claude-sonnet-5-5`. |

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
export ANTHROPIC_MODEL=claude-sonnet-5-5    # facultatif
```

Pour ne pas retaper la clé, l'ajouter à `~/.bashrc`. Ne jamais la mettre dans un fichier du dépôt.

## Utilisation dans un script Python

```python
from claude_client import ask

reponse = ask(
    system="Tu es un assistant concis.",   # consigne générale
    content="Résume ce texte : ...",        # texte, ou liste de blocs (texte + image)
    max_tokens=500,                          # longueur maximale de la réponse
)
print(reponse)
```

L'ordre de choix du modèle est le suivant : paramètre `model`, puis `ANTHROPIC_MODEL`, puis `claude-sonnet-5-5`.

## Messages d'erreur

- **« Module manquant »** : lancer `pip install -r ai/requirements.txt`.
- **« ANTHROPIC_API_KEY n'est pas définie »** : faire l'`export` ci-dessus.
