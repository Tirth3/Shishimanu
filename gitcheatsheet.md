# Git Cheat Sheet  

A quick reference for common Git commands.  

## Setup  

```bash
# Configure user information
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Check current configuration
git config --list
```

## Starting a Repository  
```bash
# Initialize a new repository
git init

# Clone an existing repository
git clone https://github.com/user/repo.git
```

## Basic Workflow
```bash
# Check the status of your repo
git status

# Stage changes (add files to next commit)
git add file.py
git add .            # add all changes

# Commit staged changes
git commit -m "Describe your changes"

# Skip staging and commit directly
git commit -am "Quick commit"
```

## Branching
```bash
# List branches
git branch

# Create a new branch
git branch feature-branch

# Switch to a branch
git checkout feature-branch

# Create and switch to a new branch
git checkout -b feature-branch

# Delete a branch
git branch -d feature-branch
```

## Remote Repositories
```bash
# View remotes
git remote -v

# Add a new remote
git remote add origin https://github.com/user/repo.git

# Push branch to remote
git push origin branch-name

# Pull changes from remote
git pull origin branch-name

# Fetch changes without merging
git fetch
```

## Merging & Rebasing
```bash
# Merge a branch into current branch
git merge feature-branch

# Rebase current branch onto another
git rebase main
```

## Undoing Changes
```bash
# Unstage a file
git reset file.py

# Discard changes in working directory
git checkout -- file.py

# Reset to last commit (dangerous, loses changes)
git reset --hard HEAD

# Revert a commit by creating a new one
git revert <commit-id>
```

## Stashing
```bash
# Save uncommitted changes
git stash

# List stashes
git stash list

# Apply latest stash
git stash apply

# Apply and drop stash
git stash pop
```

## Logs & History
```bash
# View commit history
git log

# One-line history
git log --oneline --graph --all

# Show changes in last commit
git show

# Show who changed each line in a file
git blame file.py
```

## Collaboration Workflow Example
```bash
git checkout -b feature-x          # Create feature branch
git add .                          # Stage changes
git commit -m "Add feature x"      # Commit changes
git push origin feature-x          # Push to remote
# Open a Pull Request on GitHub
```
