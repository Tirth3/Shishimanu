# Contributing to Shishimanu 🐾

Thank you for considering contributing! 🎉.  
This document outlines the contribution workflow and best practices.  
Before reading this document first read the Code Of Conduct [here](codeofconduct.md).  
For help with any git commands you can refer the following [cheat sheet](gitcheatsheet.md).  
This project follows a **simple GitHub Flow**: everything happens through branches and pull requests.


## Workflow

- **`main`** -> The default branch. All contributions are merged here.
- **`feature/*`** -> For new features.
- **`fix/*`** -> For bug fixes.
- **`doc/*`** -> For documentation updates.

👉 **Never commit directly to `main`.**  
👉 All work should be done in a branch and merged via pull request.  

## Steps to Contribute
1. **Clone the repository**
```bash
 git clone https://github.com/Tirth3/Shishimanu.git
 cd Shishimanu
 ```

2.**Create a Branch**
```bash
git checkout -b feature/your-feature-name
```
The brach name should be given according to the work that you are going to do i.e use fix/fix-name for bug fixes and feature/feature-name for features that you are adding.
Examples of branch names:
- feature/dialog-system
- fix/fullscreen-bug
- docs/readme-update

3.**Make Your Changes**  
Implement features, bug fixes, or documentation improvements.
Follow the existing code style and structure.

To run the package make a virtual environment  
```bash 
python -m venv env
```

For windows activate using following command
```bash
env\Scripts\activate.bat
env\Scripts\activate.ps1
```

For Linux/masOS activate using following command 
```bash 
source env/bin/activate
```

Now install the package using the following command
```bash 
pip install -e .
```

Now you can run the program using
```bash
shishimanu
```

There is no need to `pip install -e .` everytime to run the program.  

4.**Commit Your Changes**  
Write clear and descriptive commit messages.
```bash
git add .
git commit -m "Add dialog system for virtual pet"
```

5.**Push Your Branch**
```bash
git push origin feature/your-feature-name
```

6.**Open a Pull Request(PR)**  
- Go to the original repository on GitHub.
- Open a PR from your branch into the main branch of the project.
- Provide a description of what you changed and why.

# Code Style Guidelines
- Use meaningful variable and function names.
- Use modular programming practices.
- Add comments or docstrings where necessary.
- Keep commits small and focused.

# Reporting Issues
If you find a bug or have a feature request:  
- Check if it already exists in the [Issues](https://github.com/Tirth3/Shishimanu/issues)
- If not, create a new issue with:
  1. A clear title and description.
  2. Steps to reproduce (if it’s a bug).
  3. Expected behavior vs. actual behavior.
 
## Usefull links
1. [Pygame doc](https://www.pygame.org/docs/)
2. [Python officieal tutorial](https://docs.python.org/3/tutorial/index.html)
3. [GFG python tutorial](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/)
