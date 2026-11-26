# ai/verify_script.py

Relit un script shell **avant** de le lancer, pour repérer ce qui est dangereux. Deux niveaux :

1. **Analyse locale** : toujours faite, rien ne sort de la machine.
2. **Revue par Claude** (IA) : facultative, le contenu du script est envoyé à l'API Anthropic.

## Prérequis

```bash
python3 -m venv ~/.venvs/ai && ~/.venvs/ai/bin/pip install -r ai/requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."     # seulement pour la revue par Claude
```

## Utilisation

```bash
cd ai
~/.venvs/ai/bin/python verify_script.py --offline ../installPycharm   # analyse locale seule
~/.venvs/ai/bin/python verify_script.py ../installPycharm             # + revue par Claude
~/.venvs/ai/bin/python verify_script.py --dry-run ../installPycharm   # montre ce qui serait envoyé
~/.venvs/ai/bin/python verify_script.py --offline ../*                # tous les scripts d'un coup
```

## Options

| Option | Effet |
|---|---|
| `--offline` | Analyse locale seulement, rien n'est envoyé. |
| `--dry-run` | Affiche la requête qui serait envoyée, sans l'envoyer. |
| `--force` | Envoie même si un secret est détecté (déconseillé). |
| `--model NOM` | Choisit le modèle Claude (sinon `ANTHROPIC_MODEL`, sinon `claude-sonnet-5-5`). |
| `--lang LANGUE` | Langue de la revue (défaut : `français`). |

## Ce que l'analyse locale repère

| Gravité | Exemples |
|---|---|
| `ÉLEVÉ` | Téléchargement exécuté directement (`curl … \| sh`), `rm -rf`, opérations sur les disques (`mkfs`, `dd`, `fdisk`, `parted`). |
| `MOYEN` | Permissions `777`, `apt-key`, vérification TLS désactivée, téléchargement en `http://`, `eval`. |
| `INFO` | Accès réseau, `sudo`, absence de `set -e`. |

Les lignes de commentaire sont ignorées.

## Protections

- Fichiers de plus de 60 000 octets et fichiers binaires ignorés.
- Un fichier qui semble contenir un **secret** (clé privée, clé API, mot de passe) n'est **pas envoyé** à l'API, sauf avec `--force`.
- La consigne donnée à Claude précise que le script est une donnée à analyser : une instruction cachée dedans ne doit pas être suivie.

## Code de sortie

- `0` : aucun risque `ÉLEVÉ`.
- `1` : au moins un risque `ÉLEVÉ`. Pratique dans un autre script : `verify_script.py --offline x && ./x`.

## Ce que le script modifie

Rien sur la machine. Il lit les fichiers et affiche le résultat.
