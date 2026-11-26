"""Petit client partagé pour l'API Anthropic (utilisé par verify_script.py et ocr_ai.py).

Ce fichier ne se lance pas seul : il fournit la fonction ask() aux autres outils.
Manuel : docs/claude_client.md

Variables d'environnement :
  ANTHROPIC_API_KEY  clé API (obligatoire pour les fonctions IA)
  ANTHROPIC_MODEL    modèle à utiliser (défaut : claude-sonnet-5-5)
"""
import os
import sys

# Modèle utilisé si ni --model ni ANTHROPIC_MODEL ne sont fournis.
DEFAULT_MODEL = "claude-sonnet-5-5"


def ask(system, content, model=None, max_tokens=2000):
    """Envoie `content` (str ou liste de blocs) à Claude et renvoie le texte de la réponse.

    system     : consigne générale donnée au modèle
    content    : texte, ou liste de blocs (texte + image) pour la lecture d'images
    model      : modèle choisi ; sinon ANTHROPIC_MODEL ; sinon DEFAULT_MODEL
    max_tokens : longueur maximale de la réponse
    """
    # Le module anthropic n'est importé qu'ici : les outils restent utilisables
    # hors ligne même s'il n'est pas installé.
    try:
        import anthropic
    except ImportError:
        sys.exit("Module manquant : pip install -r requirements.txt")
    # Sans clé API, on s'arrête avec un message clair plutôt qu'une erreur réseau.
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY n'est pas définie (clé à créer sur https://console.anthropic.com/).")

    # Le client lit la clé dans ANTHROPIC_API_KEY.
    client = anthropic.Anthropic()
    message = client.messages.create(
        model=model or os.environ.get("ANTHROPIC_MODEL", DEFAULT_MODEL),
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": content}],
    )
    # La réponse peut contenir plusieurs blocs : on ne garde et ne colle que le texte.
    return "".join(block.text for block in message.content if block.type == "text")
