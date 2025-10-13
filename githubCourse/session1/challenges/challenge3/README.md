# 🧩 Challenge 3 — Shaping Commits | Découper ses Commits

This challenge is bilingual. English first, puis la version française plus bas.

---

## EN — Goal

Practice staging carefully (not everything at once), splitting work into meaningful commits.

## EN — Context

You’ll build a tiny project with three independent text files. Commit each part separately so history tells a clear story.

## EN — Tasks

1. In `work/`, create a folder `features/` with files and content:
   - `DarkMode.txt`
     - Enable dark mode option in settings
   - `About.txt`
     - About: This app helps you track habits
   - `Contact.txt`
     - Contact: support@example.com
2. Commit in three steps:
   - Commit 1: only add `DarkMode.txt` with message like "Add DarkMode feature note".
   - Commit 2: only add `About.txt`.
   - Commit 3: only add `Contact.txt`.
3. Now modify all three files at once by adding one extra line to each:

   - `DarkMode.txt` -> Default: dark mode OFF
   - `About.txt` -> Updated: v1.0 launching soon
   - `Contact.txt` -> Hours: 9am–5pm UTC

4. Stage and commit the files one by one in three separate commits (selective staging).

EN — Hints

- Stage selectively: git add path/to/file
- Commit message tip: imperative mood, short summary first line

---

## FR — Objectif

S’entraîner à indexer avec précision (pas tout d’un coup), découper le travail en commits pertinents.

## FR — Contexte

Vous allez créer un mini projet avec trois fichiers texte indépendants. Validez chaque partie séparément pour une histoire claire.

## FR — Tâches

1. Dans `work/`, créez un dossier `features/` avec fichiers et contenu :
   - `DarkMode.txt`
     - Activer l’option mode sombre dans les réglages
   - `About.txt`
     - À propos : Cette app aide à suivre vos habitudes
   - `Contact.txt`
     - Contact : support@example.com
2. Faites trois commits :
   - Commit 1 : seulement `DarkMode.txt` avec un message du type « Ajouter note DarkMode ».
   - Commit 2 : seulement `About.txt`.
   - Commit 3 : seulement `Contact.txt`.
3. Modifiez les trois fichiers en ajoutant une ligne à chacun :

   - `DarkMode.txt` -> Par défaut : mode sombre DÉSACTIVÉ
   - `About.txt` -> Mise à jour : v1.0 arrive bientôt
   - `Contact.txt` -> Horaires : 9h–17h UTC

4. Indexez et validez-les fichiers par un en trois commits séparés (index sélectif).
