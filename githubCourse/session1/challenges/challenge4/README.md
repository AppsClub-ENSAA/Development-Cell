# 🧩 Challenge 4 — Inspect, Undo, Revert | Inspecter, Annuler, Revenir

This challenge is bilingual. English first, puis la version française plus bas.

---

## EN — Goal

Use `git log` to inspect history and `git revert` to undo a specific commit safely.

## EN — Tasks

1. In `work/`, create a folder `release/` and initialize a repo inside it.
2. Create `Roadmap.txt` with exactly this line, then stage and commit:
   - Roadmap: Launch v1.0 with Dark Mode
3. Create `BugReport.txt` with exactly this line, then stage and commit:
   - BUG: Signup form crashes on submit
4. Create `Changelog.txt` with exactly this line, then stage and commit:
   - Changelog: Added About page
5. Inspect the history:
   - git log --graph --oneline --decorate --all
6. Decide that the bug report commit should be reverted (it was filed in the wrong repo). Revert only that commit:
   - git revert <hash-of-bug-commit>
7. Confirm results:
   - git log --graph --oneline --decorate --all
   - `BugReport.txt` should now be removed or its addition undone by the revert commit.

EN — Hints

- Pretty log: git log --graph --oneline --decorate --all
- Revert safely (creates a new commit): git revert <hash>
- Status : git status

---

## FR — Objectif

Utiliser `git log` pour inspecter l’historique et `git revert` pour annuler un commit précis en toute sécurité.

## FR — Tâches

1. Dans `work/`, créez un dossier `release/` et initialisez un dépôt dedans.
2. Créez `Roadmap.txt` avec exactement cette ligne, puis indexez et validez :
   - Feuille de route : Lancer v1.0 avec mode sombre
3. Créez `BugReport.txt` avec exactement cette ligne, puis indexez et validez :
   - BUG : Le formulaire d’inscription plante à l’envoi
4. Créez `Changelog.txt` avec exactement cette ligne, puis indexez et validez :
   - Journal des changements : Ajout de la page À propos
5. Inspectez l’historique :
   - git log --graph --oneline --decorate --all
6. Décidez que le commit du bug doit être annulé (mauvais dépôt). Annulez uniquement ce commit :
   - git revert <hash-du-commit-bug>
7. Vérifiez le résultat :
   - git log --graph --oneline --decorate --all
   - `BugReport.txt` doit maintenant être supprimé ou son ajout annulé par le commit de revert.

FR — Indices

- Joli log : git log --graph --oneline --decorate --all
- Annuler proprement (crée un nouveau commit) : git revert <hash>
- État: git status
