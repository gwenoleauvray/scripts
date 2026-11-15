"""Petit client partagé pour l'API Anthropic (utilisé par verify_script.py et ocr_ai.py).

Variables d'environnement :
  ANTHROPIC_API_KEY  clé API (obligatoire pour les fonctions IA)
  ANTHROPIC_MODEL    modèle à utiliser (défaut : claude-sonnet-5-5)
"""
import os
import sys

DEFAULT_MODEL = "claude-sonnet-5-5"


def ask(system, content, model=None, max_tokens=2000):
    """Envoie `content` (str ou liste de blocs) à Claude et renvoie le texte de la réponse."""
    try:
        import anthropic
    except ImportError:
        sys.exit("Module manquant : pip install -r requirements.txt")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY n'est pas définie (clé à créer sur https://console.anthropic.com/).")

    client = anthropic.Anthropic()
    message = client.messages.create(
        model=model or os.environ.get("ANTHROPIC_MODEL", DEFAULT_MODEL),
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": content}],
    )
    return "".join(block.text for block in message.content if block.type == "text")
