## 🚀 **Challenge 1 — Create a Repository and Push Changes**

**Goal:**
Learn how to connect your local project with GitHub — whether you start by creating the repo online or already have one on your computer.

---

### 🧭 **Option 1 — Start from GitHub**

1. **Create a new repository** on GitHub called `my-first-repo`.
2. **Clone it to your local machine:**

   ```bash
   git clone https://github.com/YOUR-USERNAME/my-first-repo.git
   cd my-first-repo
   ```
3. **Create a file** named `README.md` and write a short introduction about yourself.
4. **Stage and commit your changes:**

   ```bash
   git add README.md
   git commit -m "Add README with introduction"
   ```
5. **Push your changes to GitHub:**

   ```bash
   git push origin main
   ```
6. **Verify** that your file appears on GitHub. ✅

---

### 💻 **Option 2 — Start from Your Local Project**

1. **Go to your existing project folder:**
   - Open VS Code → File → Open Folder → Select your project folder.

2. **Initialize it as a Git repository (if not already):**

   ```bash
   git init
   ```
3. **Create a new repository on GitHub** (without adding a README or .gitignore).
4. **Connect your local repo to GitHub:**

   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/your-project.git
   ```
5. **Stage, commit, and push your local files:**

   ```bash
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git push -u origin main
   ```
6. **Check** that your local files now appear in your GitHub repository. ✅

---

