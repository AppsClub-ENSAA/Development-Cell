# 🧩 Challenge 5 — Team Members Line-up | Classement des Membres

This challenge is bilingual. English first, puis la version française.

---

## EN — Goal

Merge the prepared `newBranch` branch into `main` and resolve the conflict in `TeamMembers.txt`. Explore the file contents and figure out the **official order of the team members** yourself.

## EN — Tasks

1. Create and enter a new folder for this challenge:
   - mkdir ../challenge5 && cd ../challenge5
2. Clone the challenge repository inside it:

```bash
git clone git@github.com:Houcineee/AppsTeamChallenge.git
```

3. Enter the cloned folder:

```bash
cd AppsTeamChallenge
```

4. Explore the branches and see which ones exist:

```bash
git branch -a
```

5. Switch to the `newBranch` branch (this will create a local branch tracking the remote):

```bash
git switch newBranch
```

6. Switch back to `main` and merge `newBranch`:

```bash
git switch main
git merge newBranch
```

7. Resolve the conflict in `TeamMembers.txt` by arranging the members in the correct order.
8. Complete the merge and check the final content and history.

---

## FR — Objectif

Fusionner la branche `newBranch` dans `main` et résoudre le conflit dans `TeamMembers.txt`. Explorez le contenu des fichiers pour **trouver vous-même le bon ordre des membres**.

## FR — Tâches

1. Créez et entrez dans un nouveau dossier pour ce challenge :
   - mkdir ../challenge5 && cd ../challenge5
2. Clonez le dépôt du challenge dedans :

```bash
git clone git@github.com:Houcineee/AppsTeamChallenge.git
```

3. Entrez dans le dossier cloné :

```bash
cd AppsTeamChallenge
```

4. Explorez les branches et vérifiez lesquelles existent :

```bash
git branch -a
```

5. Basculez sur la branche `newBranch` (cela créera une branche locale suivie de la branche distante) :

```bash
git switch newBranch
```

6. Revenez sur `main` et fusionnez `newBranch` :

```bash
git switch main
git merge newBranch
```

7. Résolvez le conflit dans `TeamMembers.txt` en réorganisant correctement les membres.
8. Terminez la fusion et vérifiez le contenu final et l’historique.
