# Session 1 — Command Cheat Sheet

Quick reference for Linux + Git commands used in this session.

## Linux basics

```bash
# list files
ls
# make directory
mkdir <folder>
# change directory
cd <folder>
# go up one level
cd ..
# create empty file
touch <file>
# edit a file
notepad  fileName
```

## Git setup (once)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "notepad"   # or another editor
git config --global init.defaultBranch main
```

## Start a repo + first commits

```bash
# initialize repo in current folder
git init
# check status
git status
# stage a specific file
git add <file>
# stage everything in the folder
git add .
# commit with a message
git commit -m "Your message"
```

## See changes and history

```bash
# compact history
git log --oneline
# pretty graph across branches
git log --graph --oneline --decorate --all
```

## Branching and switching

````bash
# list branches
git branch
# create and switch to a new branch
git switch -c <branch>
# switch to an existing branch
git switch <branch>


## Merging

```bash
# merge another branch into the current branch
git merge <branch>
````

## Selective staging vs. add all

```bash
# add just one file
git add <path/to/file>
# add everything in the working directory
git add .
```

## Undo (safe)

```bash
# create a new commit that reverses a past commit
git revert <commit-hash>
```

## Conflict resolution (manual steps)

```bash
# when merge reports conflicts:
# 1) open the conflicted file(s) and edit to the final content
# 2) stage resolved files
git add <file>
# 3) complete the merge (commit message auto-filled)
git commit
```
