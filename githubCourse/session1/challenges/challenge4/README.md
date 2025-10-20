# 🧩 Challenge 4 — Branches: Safe Parallel Work | Branches: Travail en parallèle

This challenge is bilingual. English first, puis la version française plus bas.

---

## EN — Goal

Understand why branches exist, create a feature branch, and keep `main` clean while developing.

## EN — Tasks

1. Create and enter a new folder for this challenge:
   - mkdir ../challenge4 && cd ../challenge4
   - git init
2. Create `DarkMode.txt` with the content below and commit it:
   - DarkMode: planned for v1.0
3. Create and switch to a new branch `feature/about`.
4. Create `About.txt` with exactly:
   - About: This app tracks habits
     Commit on `feature/about`.
5. Switch back to `main` and confirm `About.txt` is not there (main remains untouched).
6. Switch to `feature/about` again and append this line to `About.txt`:
   - Updated: v1.0 coming soon
     Commit again.
7. Merge the feature branch into `main` (switch to `main`, then merge `feature/about`).
8. Visualize branches after the merge: `git log --graph --oneline --decorate --all`.
9. Confirm on `main` that `About.txt` is present with both lines.

EN — Hints

- Create and switch: git switch -c feature/about (or: git checkout -b feature/about)
- Switch back: git switch main
- Merge: git switch main && git merge feature/about
- See branches: git branch
- Pretty graph: git log --graph --oneline --decorate --all

## FR — Objectif

Comprendre l’utilité des branches, créer une branche de fonctionnalité et garder `main` propre pendant le dev.

## FR — Tâches

1. Créez et entrez dans un nouveau dossier pour ce challenge :
   - mkdir ../challenge4 && cd ../challenge4
   - git init
2. Créez `DarkMode.txt` avec le contenu ci-dessous et validez :
   - ModeSombre : prévu pour v1.0
3. Créez et basculez sur une nouvelle branche `feature/about`.
4. Créez `About.txt` avec exactement :
   - À propos : Cette app suit les habitudes
     Validez sur `feature/about`.
5. Revenez sur `main` et vérifiez que `About.txt` n’y est pas (main reste intacte).
6. Revenez sur `feature/about` et ajoutez cette ligne à `About.txt` :
   - Mise à jour : v1.0 arrive bientôt
     Validez encore.
7. Fusionnez la branche de fonctionnalité dans `main` (basculez sur `main`, puis fusionnez `feature/about`).
8. Visualisez les branches après la fusion : `git log --graph --oneline --decorate --all`.
9. Vérifiez sur `main` que `About.txt` est présent avec les deux lignes.

FR — Indices

- Créer et basculer : `git switch -c feature/about` (ou : `git checkout -b feature/about`)
- Revenir sur main : `git switch main`
- Fusionner : `git switch main && git merge feature/about`
- Lister les branches : `git branch`
- Beau graphe : `git log --graph --oneline --decorate --all`
