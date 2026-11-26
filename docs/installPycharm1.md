# installPycharm1 — ancienne version

> ⚠ **Obsolète.** Utiliser [`installPycharm`](installPycharm.md).

Première version du script d'installation de PyCharm, conservée pour mémoire.

## Ce qu'il fait

1. Installe `snapd` (demande une confirmation).
2. Installe `snapd-xdg-open`, un paquet ancien souvent absent des Debian récentes.
3. Installe PyCharm par snap.
4. Lance PyCharm.

## Pourquoi ne plus l'utiliser

- Il continue même si une étape échoue.
- Il ne crée pas le lien `/snap` dont les snaps « classic » ont besoin sous Debian.
- L'étape `snapd-xdg-open` échoue sur les systèmes récents.
