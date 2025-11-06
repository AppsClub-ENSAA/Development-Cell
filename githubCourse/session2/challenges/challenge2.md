## 👥 Challenge 2 — Collaborate on GitHub (No Branches)

**Goal:** Work directly on a shared repository without using branches.

### Steps:

1. Ask a friend to add you as a **collaborator** on their repository.
2. Clone their repository:

   ```bash
   git clone https://github.com/FRIEND-USERNAME/REPOSITORY-NAME.git
   ```
3. Create a new file called `contributors.txt` and add both of your names.
4. Commit and push your changes:

   ```bash
   git add contributors.txt
   git commit -m "Add contributors list"
   git push origin main
   ```
5. Check that your update appears in the GitHub repository.

💡 *Tip:* If you and your friend edit the same file at the same time, you might get a **merge conflict** — that’s normal! Try to resolve it locally, then push again.


