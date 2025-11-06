## 🧩 **Challenge 3 — Collaborate Like a Pro Using Branches and Pull Requests**

**Goal:**
Learn to collaborate safely on a shared GitHub project where both of you are contributors, using branches and pull requests instead of pushing directly to `main`.

---

### 👤 **Friend A (the project owner)**

1. **Create a new GitHub repository.**
2. **Add your friend as a collaborator.**

   > Settings → Collaborators → Add collaborator
3. **Share the repository link** with your friend.
4. **Wait for their pull request.**
5. **Review and approve** the PR once it looks good.

---

### 👤 **Friend B (the collaborator)**

1. **Clone the repository**

   ```bash
   git clone https://github.com/ORG-OR-USERNAME/REPO-NAME.git
   cd REPO-NAME
   ```

2. **Create a new branch**

   ```bash
   git checkout -b feature/update-readme
   ```

3. **Make a small change**
   For example, fix a typo or add a new line in `README.md`.

4. **Stage and commit**

   ```bash
   git add .
   git commit -m "Fix typo in README"
   ```

5. **Push the branch to GitHub**

   ```bash
   git push origin feature/update-readme
   ```

6. **Open a Pull Request**

   * Go to the repo on GitHub.
   * Click **“Compare & pull request.”**
   * Target the `main` branch.
   * Add a short explanation of your change.

7. **Wait for approval** from Friend A.

8. **Clean up (optional)**

   ```bash
   git checkout main
   git pull origin main
   git branch -d feature/update-readme
   ```

---

