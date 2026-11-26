# checkJava4Shell

Cherche sur toute la machine si elle est exposée à la faille **Java4Shell** (CVE-2026-114938, publiée le 17 novembre 2026) et s'il y a des traces de tentative d'attaque.

## À quoi ça sert

Java4Shell est une faille de Java qui peut permettre à un attaquant de prendre la main sur un serveur, sans mot de passe. Le script répond à deux questions :

1. **Suis-je vulnérable ?** Il regarde le processeur et toutes les versions de Java présentes, y compris celles cachées dans des applications.
2. **Ai-je été visé ?** Il cherche des plantages de Java, des traces d'attaque dans les journaux, et un faux outil malveillant connu.

## Sécurité

- **Lecture seule** : il ne modifie, ne supprime et n'installe rien.
- Il **n'exécute aucun programme Java** trouvé sur le disque : il lit leur version dans leurs fichiers `release`.
- Seule écriture : son rapport dans `/tmp`.

## Prérequis

- Linux (Debian, Ubuntu, Raspberry Pi OS…).
- Les droits administrateur (`sudo`) pour tout lire. Sans `sudo`, le résultat est incomplet et le script le signale.

## Utilisation

```bash
sudo bash checkJava4Shell
```

La recherche sur tout le disque peut prendre quelques minutes.

## Les 7 contrôles

| N° | Contrôle | Ce qui est vérifié |
|---|---|---|
| 1 | Processeur | La faille ne s'exploite que sur x86-64 avec AVX-512 VBMI. Un Raspberry Pi (ARM) n'est pas concerné. |
| 2 | Recherche disque | Un seul passage sur tout le disque (hors `/proc`, `/sys`, `/dev`, `/run`). |
| 3 | Versions de Java | Comparées aux versions corrigées : 17.0.21.1, 21.0.13.1, 25.0.5.1, 27.0.1.1. Java 8, 11 et 17.0.0 à 17.0.5 ne sont pas concernés, ni OpenJ9. |
| 4 | Programmes Java en marche | Options de protection actives, shells lancés par Java, ports ouverts, connexions. |
| 5 | Plantages | Fichiers `hs_err_pid*.log` et plantages dans le journal système depuis le 17/11/2026. |
| 6 | Journaux `/var/log` | Motifs d'attaque connus (mot « java4shell », 64 « A » suivis de « = »…). |
| 7 | Faux outil | Présence du leurre malveillant `java4shell-exposure-audit`. |

## Lire le résultat

| Étiquette | Signification |
|---|---|
| `[OK]` | Rien à faire. |
| `[INFO]` | Renseignement, à regarder si besoin. |
| `[VULNÉRABLE]` | Un Java à mettre à jour, ou un processeur exploitable. |
| `[ALERTE]` | Signe suspect à examiner. **Ce n'est pas une preuve d'infection.** |

Le bilan final compte les `VULNÉRABLE` et les `ALERTE`. Le rapport complet est dans `/tmp/java4shell-<machine>-<date>.txt`.

## Que faire si…

- **Un Java est vulnérable** : `sudo apt update && sudo apt full-upgrade`, ou mettre à jour l'application qui embarque ce Java.
- **En attendant la mise à jour**, si le processeur est exploitable : ajouter l'option `-XX:-UseBASE64Intrinsics` au lancement du programme Java, puis le redémarrer.
- **Une alerte apparaît** : garder le rapport et le faire analyser.

## Limites

Aucun indicateur de compromission (empreinte de fichier, adresse IP) n'a été publié pour cette faille. Le script repère une **exposition** et des **signes suspects**, pas un virus précis. Un Java sans fichier `release` est signalé `[INFO]` : sa version est à vérifier à la main.
